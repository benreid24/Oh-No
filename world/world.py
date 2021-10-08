from camera import Camera
import pygame

from camera import Camera
from component.controller import Controller
from component.local_controller import LocalController
from component.physics import Physics
from component.position import Position
from component.image_graphic import ImageGraphic
from component.regular_physics import RegularPhysics
from component.ship_stats import ShipStats
from entity.entity import Entity
from constants import BLACK

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
        self.camera = Camera()

    def update(self, dt):
        # type: (float) -> None

        for entity in self.entities:
            entity.update(dt)
        self.camera.update(dt)

        return True

    def render(self, screen):
        # type: (any) -> None

        screen.fill(BLACK)
        for entity in self.entities:
            entity.render(screen, self.camera)
        pygame.display.flip()

    def spawn_entity(self, entity):
        # type: (Entity) -> None
        self.entities.append(entity)
