import pygame

from .graphics import Graphics
from camera import Camera
from entity.entity import Entity


class ImageGraphic(Graphics):
    """
    Basic static image graphics component
    """

    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(filename)

    def render(self, screen, camera, owner):
        # type: (any, Camera, Entity) -> None

        rect = self.image.get_rect(
            center=camera.transform(owner.position)
        )
        center = rect.center
        rotated_image = pygame.transform.rotate(self.image, -owner.position.angle)
        rotated_rect = rotated_image.get_rect(center=center)

        screen.blit(rotated_image, rotated_rect)
