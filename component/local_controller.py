import pygame
from pygame.key import get_pressed

from .controller import Controller


class LocalController(Controller):
    def __init__(self):
        super().__init__()
        self.accel = pygame.K_UP
        self.rotate_left = pygame.K_LEFT
        self.rotate_right = pygame.K_RIGHT
        self.primary_fire = pygame.K_SPACE
        self.secondary_fire = pygame.K_v

    def update(self, dt, owner):
        keys = get_pressed()

        if keys[self.accel]:
            Controller.accelerate(owner)
        else:
            Controller.freeze(owner)

        if keys[self.rotate_left]:
            Controller.rotate(owner, dt, True)
        if keys[self.rotate_right]:
            Controller.rotate(owner, dt, False)
        if keys[self.primary_fire]:
            pass  # TODO - fire weapon
        if keys[self.secondary_fire]:
            pass  # TODO - fire weapon
