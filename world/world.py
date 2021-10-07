from camera import Camera
import pygame

from camera import Camera
from component.position import Position
from entity.entity import Entity
from constants import BLACK

class World:
    def __init__(self) -> None:
        self.player = Entity(Position(300, 300, 0), pygame.image.load('resources/player_ship.png'))
        self.player_lives = 3
        self.entities = [self.player]
        self.camera = Camera(self.player)

    def update(self, dt: float):
        for entity in self.entities:
            entity.update(dt)
        self.camera.update(dt)

        return True

    def render(self, screen):
        screen.fill(BLACK)
        for entity in self.entities:
            entity.render(screen, self.camera)
        pygame.display.flip()

    def spawn_entity(self, entity: Entity):
        self.entities.append(entity)
