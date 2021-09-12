from camera import Camera
import pygame

from camera import Camera
from entity.entity import Entity
from .stage import Stage
from .stages.stage1 import Stage1
from constants import BLACK

class World:
    def __init__(self) -> None:
        self.stages = [Stage1()]
        self.player = Entity((300, 300), pygame.image.load('resources/player_ship.png'))
        self.player_lives = 3
        self.entities = [self.player]
        self.camera = Camera(self.player)

        self.stages[0].initialize(self)

    def update(self, dt):
        for entity in self.entities:
            entity.update(dt)
        self.camera.update(dt)

        if not self.stages[0].active():
            self.stages.pop(0)
            if not self.stages:
                return False
            else:
                self.entities = [self.player]
                self.stages[0].initialize(self)

        return True

    def render(self, screen):
        screen.fill(BLACK)
        for entity in self.entities:
            entity.render(screen, self.camera)
        pygame.display.flip()

    def spawn_entity(self, entity: Entity):
        self.entities.append(entity)
