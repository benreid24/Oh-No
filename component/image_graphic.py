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

        scaled_image = pygame.transform.scale(
            self.image,
            camera.transform_entity_size_tuple(owner, (self.image.get_width(), self.image.get_height()))
        )
        scaled_rect = scaled_image.get_rect(center=camera.transform_point(owner.position))
        rotated_image = pygame.transform.rotate(scaled_image, -owner.position.angle)
        rotated_rect = rotated_image.get_rect(center=scaled_rect.center)
        screen.blit(rotated_image, rotated_rect)
