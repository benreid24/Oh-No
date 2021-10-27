from typing import Tuple

import pygame

from .graphics import Graphics
from camera import Camera
from entity.entity import Entity


class CircleGraphic(Graphics):
    """
    Basic circle graphic
    """

    def __init__(self, color, radius):
        # type: (Tuple[int,int,int], int) -> None

        super().__init__()
        self.color = color
        self.radius = radius

    def render(self, screen, camera, owner):
        # type: (any, Camera, Entity) -> None

        pygame.draw.circle(
            screen,
            self.color,
            camera.transform_point(owner.position),
            camera.transform_entity_scalar(owner, self.radius)
        )
