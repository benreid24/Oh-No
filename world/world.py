import math
from random import choice, uniform

import pygame
import scipy.stats as stats

from camera import Camera
from component.controller import Controller
from component.local_controller import LocalController
from component.orbital_physics import OrbitalPhysics
from component.physics import Physics
from component.position import Position
from component.image_graphic import ImageGraphic
from component.regular_physics import RegularPhysics
from component.ship_stats import ShipStats
from entity.entity import Entity
from constants import BLACK
from .starfield import Starfield
from component.collidable import Collidable

class World:
    """
    The entire world. This will likely evolve
    """

    def __init__(self):
        self.player = Entity(Position(300, 300, 0), ImageGraphic('resources/player_ship.png'))
        self.player.components[Controller] = LocalController()
        self.player.components[ShipStats] = ShipStats()
        self.player.components[Physics] = RegularPhysics()
        self.player_lives = 3
        self.entities = [self.player]
        self.camera = Camera(self.player)
        self.stars = Starfield(100, self.camera.get_area())

    def update(self, dt):
        # type: (float) -> None

        for entity in self.entities:
            entity.update(dt)
        self.camera.update(dt)
        self.stars.update(dt)

        return True

    def render(self, screen):
        # type: (any) -> None

        screen.fill(BLACK)
        self.stars.render(screen, self.camera)
        for entity in self.entities:
            entity.render(screen, self.camera)
        pygame.display.flip()

    def spawn_entity(self, entity):
        # type: (Entity) -> None
        self.entities.append(entity)

    def generate_world(self):
        system_rotation = choice([True, False])
        star_count = 1
        star_radius = 425
        star_mass = 5
        star = Entity(position = Position(0,0,0), graphic = ImageGraphic('resources/bases/red_base_1.png'))
        star.components[Collidable] = Collidable(Collidable.BoundType.Circle, radius = star_radius, mass = star_mass)
        self.entities.append(star)
        prad_min = 142
        prad_max = 182
        pdist_min = 3600
        pdist_max = 4900

        planet_count = int(stats.binom.rvs(n = 5, p = .5,size = 1)[0] + 5)
        planet_list = []
        p_tot_dist = 0
        for p in range(planet_count):
            p_radius = int(uniform(prad_min, prad_max))
            p_dist = int(uniform(pdist_min, pdist_max))
            p_tot_dist += p_dist
            p_angle_r = uniform(0, 2*math.pi)
            p_angle = p_angle_r * 180 / math.pi
            p_mass = 2
            p_x = math.cos(p_angle_r)*p_tot_dist
            p_y = math.sin(p_angle_r)*p_tot_dist
            planet = Entity(position = Position(p_x,p_y,p_angle), graphic = ImageGraphic('resources/bases/red_base_1.png'))
            planet.components[Collidable] = Collidable(Collidable.BoundType.Circle, radius = p_radius, mass = p_mass)
            planet.components[Physics] = OrbitalPhysics(parent = star, owner = planet, clockwise = system_rotation)
            planet_list.append(planet)
            self.entities.append(planet)
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
                m_mass = .2
                m_x = p_x + math.cos(m_angle_r)*m_tot_dist
                m_y = p_y + math.sin(m_angle_r)*m_tot_dist
                moon = Entity(position = Position(m_x, m_y, m_angle), graphic = ImageGraphic('resources/bases/red_base_1.png'))
                planet.components[Collidable] = Collidable(Collidable.BoundType.Circle, radius = m_radius, mass = m_mass)
                planet.components[Physics] = OrbitalPhysics(parent = planet, owner = moon, clockwise = system_rotation)
                self.entities.append(moon)
