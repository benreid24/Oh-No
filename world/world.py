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
from component.collidable import Collidable, BoundingArea

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
        self.stars = Starfield(300, self.camera.get_area())

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
        star_radius = 5
        star_mass = 5
        star = Entity(position = Position(0,0,0), graphic = ImageGraphic('resources/bases/red_base_1.png'))
        star.components[Collidable] = Collidable(BoundingArea(BoundingArea.BoundType.Circle, radius = star_radius), mass = star_mass)
        self.entities.append(star)
        p_min = star_radius * 1.5
        p_max = 35

        planet_count = stats.binom.rvs(7,.5,1)
        planet_list = []
        for p in range(planet_count):
            p_dist = uniform(p_min, p_max)
            p_angle_r = uniform(0, 2*math.pi)
            p_angle = p_angle_r * 180 / math.pi
            p_mass = 6.08 * (p_dist/p_max)**2 - 5.74 * (p_dist/p_max)**3
            p_radius = (2.355*p_mass)**(1/3)
            p_x = math.cos(p_angle_r)*p_radius
            p_y = math.sin(p_angle_r)*p_radius
            planet = Entity(position = Position(p_x,p_y,p_angle), graphic = ImageGraphic('resources/bases/red_base_1.png'))
            planet.components[Collidable] = Collidable(BoundingArea(BoundingArea.BoundType.Circle, radius = p_radius), mass = p_mass)
            planet.components[Physics] = OrbitalPhysics(parent = star, owner = planet, clockwise = system_rotation)
            planet_list.append(planet)
            self.entities.append(planet)
            p_moon_count = int(stats.uniform.rvs(0,4*p_mass,1)[0])
            for m in range(p_moon_count):
                m_min = 2*p_radius
                m_max = 4*p_radius
                m_dist = uniform(m_min, m_max)
                m_angle_r = uniform(0, 2*math.pi)
                m_angle = m_angle_r * 180 / math.pi
                m_mass = 6.08 * (m_dist/m_max)**2 - 5.74 * (m_dist/m_max)**3
                m_radius = stats.truncnorm.rvs(a = p_radius/5, b = p_radius/3, size = 1)[0]
                m_x = p_x + math.cos(m_angle_r)*m_radius
                m_y = p_y + math.sin(m_angle_r)*m_radius
                moon = Entity(position = Position(m_x, m_y, m_angle), graphic = ImageGraphic('resources/bases/red_base_1.png'))
                planet.components[Collidable] = Collidable(BoundingArea(BoundingArea.BoundType.Circle, radius = m_radius), mass = m_mass)
                planet.components[Physics] = OrbitalPhysics(parent = planet, owner = moon, clockwise = system_rotation)
                self.entities.append(moon)