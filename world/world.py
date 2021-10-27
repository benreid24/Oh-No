import math
from random import choice, uniform, randrange
from typing import List

import pygame
import scipy.stats as stats

from camera import Camera
from component.circle_graphic import CircleGraphic
from component.controller import Controller
from component.flashing_graphic import FlashingGraphic
from component.local_controller import LocalController
from component.minimap import ShowsOnMinimap
from component.orbital_physics import OrbitalPhysics
from component.physics import Physics
from component.position import Position, Vector
from component.image_graphic import ImageGraphic
from component.regular_physics import RegularPhysics
from component.ship_stats import ShipStats
from entity.entity import Entity
from constants import BLACK, DEFAULT_VIEWPORT, MINIMAP_SIZE, SIDE_PANEL_BACKGROUND, SIDE_PANEL_BORDER, SIDE_PANEL_SIZE, WHITE, WINDOW_RESOLUTION
from event.events.entity_spawn import EntitySpawnEvent
from world.minimap import Minimap
from .starfield import Starfield
from component.collidable import Collidable
from event.bus import EventBus

class World:
    """
    The entire world. This will likely evolve
    """

    def __init__(self):
        self.entities = [] # type: List[Entity]
        self.event_bus = EventBus()
        self.minimap = Minimap(self.event_bus)

        self.world_clip = 0, 0, DEFAULT_VIEWPORT[0], DEFAULT_VIEWPORT[1]
        self.side_panel_clip = DEFAULT_VIEWPORT[0], 0, SIDE_PANEL_SIZE[0], SIDE_PANEL_SIZE[1]
        self.side_panel_border = (
            self.side_panel_clip[0] - 2,
            self.side_panel_clip[1],
            self.side_panel_clip[2],
            self.side_panel_clip[3]
        )
        self.minimap_clip = (
            DEFAULT_VIEWPORT[0],
            WINDOW_RESOLUTION[1] - MINIMAP_SIZE[1],
            MINIMAP_SIZE[0],
            MINIMAP_SIZE[1]
        )

        self.player = Entity(Position(300, 300, 0), ImageGraphic('resources/player_ship.png'))
        self.player.components[Controller] = LocalController()
        self.player.components[ShipStats] = ShipStats()
        self.player.components[Physics] = RegularPhysics()
        self.player.components[ShowsOnMinimap] = ShowsOnMinimap(
            render_override=FlashingGraphic(0.4, CircleGraphic(WHITE, 145))
        )
        self.player_lives = 3

        self.camera = Camera()
        self.stars = Starfield(100, self.camera.get_visible_area())
        self.planet_list = [] # type: List[Entity]

    def update(self, dt):
        # type: (float) -> None

        for entity in self.entities:
            entity.update(dt)
        self.camera.update(dt)
        self.stars.update(dt)

        return True

    def render(self, screen):
        # type: (any) -> None

        screen.set_clip(None)
        screen.fill(BLACK)
        
        screen.set_clip(self.world_clip)
        self.stars.render(screen, self.camera)
        for entity in self.entities:
            entity.render(screen, self.camera)

        # screen.set_clip(None)
        pygame.draw.rect(screen, SIDE_PANEL_BORDER, self.side_panel_border, width=2)
        screen.set_clip(self.side_panel_clip)
        pygame.draw.rect(screen, SIDE_PANEL_BACKGROUND, self.side_panel_clip)

        screen.set_clip(self.minimap_clip)
        self.minimap.render(screen, self.minimap_clip)

        pygame.display.flip()

    def spawn_entity(self, entity):
        # type: (Entity) -> None
        self.entities.append(entity)
        self.event_bus.push(EntitySpawnEvent, EntitySpawnEvent(entity))

    def spawn_player(self):
        # type: () -> None
        # Picking a Home Planet and placing the player near it:
        home_planet_pos = choice([0,1,2])
        home_planet = self.planet_list[home_planet_pos]
        player_dist = 200
        player_angle_r = uniform(0, 2*math.pi)
        player_angle = player_angle_r * 180 / math.pi
        self.player.position.x = home_planet.position.x + math.cos(player_angle_r)*(player_dist + home_planet.components[Collidable].radius)
        self.player.position.y = home_planet.position.y + math.sin(player_angle_r)*(player_dist + home_planet.components[Collidable].radius)
        self.player.position.angle = player_angle + 90

        self.spawn_entity(self.player)
        self.camera = Camera(self.player)
        self.camera.update(0)
        self.stars = Starfield(100, self.camera.get_visible_area())

    def generate_world(self):
        system_rotation = choice([True, False])
        star_count = 1
        star_radius = 425
        star_mass = 95_625_000
        g_color = randrange(168,253)
        star = Entity(position = Position(0,0,0), graphic = CircleGraphic((252,g_color,20),star_radius))
        star.components[ShowsOnMinimap] = ShowsOnMinimap(0.6)
        star.components[Collidable] = Collidable(Collidable.BoundType.Circle, radius = star_radius, mass = star_mass)
        self.spawn_entity(star)
        prad_min = 142
        prad_max = 182
        pdist_min = 3600
        pdist_max = 4900
        planet_count = int(stats.binom.rvs(n = 5, p = .5,size = 1)[0] + 5)
        p_tot_dist = 0
        for p in range(planet_count):
            p_radius = int(uniform(prad_min, prad_max))
            p_dist = int(uniform(pdist_min, pdist_max))
            p_tot_dist += p_dist
            p_angle_r = uniform(0, 2*math.pi)
            p_angle = p_angle_r * 180 / math.pi
            p_mass = 2_531_250
            p_x = math.cos(p_angle_r)*p_tot_dist
            p_y = math.sin(p_angle_r)*p_tot_dist
            r_color = randrange(60,220)
            g_color = randrange(60,220)
            b_color = randrange(60,220)
            planet = Entity(position = Position(p_x,p_y,p_angle), graphic = CircleGraphic((r_color,g_color,b_color),p_radius))
            planet.components[ShowsOnMinimap] = ShowsOnMinimap()
            planet.components[Collidable] = Collidable(Collidable.BoundType.Circle, radius = p_radius, mass = p_mass)
            planet.components[Physics] = OrbitalPhysics(parent = star, owner = planet, clockwise = system_rotation)
            self.planet_list.append(planet)
            self.spawn_entity(planet)
            p_moon_count = stats.binom.rvs(n = 3, p = .3,size = 1)[0] 
            mrad_min = int(p_radius/3) - 10
            mrad_max = int(p_radius/3) + 10
            mdist_min = 300
            mdist_max = 600
            m_tot_dist = 0
            for m in range(p_moon_count):
                m_dist = int(uniform(mdist_min, mdist_max))
                m_tot_dist += m_dist
                m_radius = int(uniform(mrad_min, mrad_max))
                m_angle_r = uniform(0, 2*math.pi)
                m_angle = m_angle_r * 180 / math.pi
                m_mass = 500_000
                m_x = p_x + math.cos(m_angle_r)*m_tot_dist
                m_y = p_y + math.sin(m_angle_r)*m_tot_dist
                moon = Entity(position = Position(m_x, m_y, m_angle), graphic = CircleGraphic((240,234,234), m_radius))
                moon.components[Collidable] = Collidable(Collidable.BoundType.Circle, radius = m_radius, mass = m_mass)
                moon.components[Physics] = OrbitalPhysics(parent = planet, owner = moon, clockwise = system_rotation)
                moon.components[ShowsOnMinimap] = ShowsOnMinimap()
                self.spawn_entity(moon)

        b_inside_planet = randrange(0, planet_count-2)
        abase_dist =  (self.planet_list[b_inside_planet].components[Physics].radius + self.planet_list[b_inside_planet+1].components[Physics].radius)/2
        asteroid_count = int(stats.binom.rvs(n = 20, p = .5,size = 1)[0] + 10)
        abase_rad = 10
        asteroid_list = []
        #Placing the first asteroid:
        a_radius = int(stats.binom.rvs(n = 10, p = .4, size = 1)[0])*3 + abase_rad
        a_tot_dist  = int(uniform(abase_dist - 300, abase_dist + 300))
        a_angle_r = uniform(0, 2*math.pi)
        a_angle = a_angle_r * 180 / math.pi
        a_mass = 300_000
        a_x = math.cos(a_angle_r)*a_tot_dist
        a_y = math.sin(a_angle_r)*a_tot_dist
        r_color = randrange(80,97)
        g_color = randrange(54,85)
        b_color = randrange(7,40)
        asteroid = Entity(position = Position(a_x,a_y,a_angle), graphic = CircleGraphic((r_color,g_color,b_color),a_radius))
        asteroid.components[Collidable] = Collidable(Collidable.BoundType.Circle, radius = a_radius, mass = a_mass)
        asteroid.components[Physics] = OrbitalPhysics(parent = star, owner = asteroid, clockwise = system_rotation)
        asteroid_list.append(asteroid)
        self.entities.append(asteroid)
        for a in range(asteroid_count-1):
            a_radius = int(stats.binom.rvs(n = 10, p = .4, size = 1)[0])*3 + abase_rad
            a_rel_dist  = int(uniform(40, 250))
            a_ref_axis = asteroid_list[a].components[Physics].phase
            a_rel_angle = int(uniform(math.pi/6 + a_ref_axis, 5*math.pi/6 + a_ref_axis))
            a_x = math.cos(a_rel_angle)*a_rel_dist + asteroid_list[a].position.x
            a_y = math.sin(a_rel_angle)*a_rel_dist + asteroid_list[a].position.y
            a_tot_dist = (a_x**2 + a_y**2)**.5
            a_angle = math.atan2(a_y, a_x)
            a_mass = 300_000
            r_color = randrange(80,97)
            g_color = randrange(54,85)
            b_color = randrange(7,40)
            asteroid = Entity(position = Position(a_x,a_y,a_angle), graphic = CircleGraphic((r_color,g_color,b_color),a_radius))
            asteroid.components[Collidable] = Collidable(Collidable.BoundType.Circle, radius = a_radius, mass = a_mass)
            asteroid.components[Physics] = OrbitalPhysics(parent = star, owner = asteroid, clockwise = system_rotation)
            asteroid_list.append(asteroid)
            self.entities.append(asteroid)
