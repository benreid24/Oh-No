import pygame

from entity.entity import Entity


class BasicStarbase(Entity):
    def __init__(self, position):
        super().__init__(position, pygame.image.load('Resources/bases/basic.png'))

    def update(self, dt):
        # do nothing? Maybe shoot
        pass