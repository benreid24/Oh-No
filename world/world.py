from camera import Camera
import pygame

from camera import Camera
from entity.entity import Entity
from .stage import Stage
from constants import BLACK

class World:
    def __init__(self) -> None:
        self.active_stage = Stage()
        self.player = Entity((300, 300), pygame.image.load('resources/test.png'))
        self.player_lives = 3
        self.entities = [self.player]
        self.camera = Camera(self.player)

    def update(self, dt):
        for entity in self.entities:
            entity.update(dt)
        self.camera.update(dt)

        if not self.active_stage.active():
            # TODO - victory screen and next stage
            pass

    def render(self, screen):
        screen.fill(BLACK)
        for entity in self.entities:
            entity.render(screen, self.camera)
        pygame.display.flip()
