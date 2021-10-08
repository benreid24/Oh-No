from typing import Type, Dict

from camera import Camera
from component.position import Position
from component.component import Component
from component.controller import Controller
from component.physics import Physics
from component.graphics import Graphics

class Entity:
    """
    Entity class for all entities in the game. Owns components to get functionality
    """

    def __init__(self, position, graphic):
        # type: (Position, Graphics) -> None

        self.position = position
        self.alive = True
        self.components: Dict[Type, Component] = {
            Controller: Controller(),
            Physics: Physics(),
            Graphics: graphic
        }

    def update(self, dt):
        # type: (float) -> None

        for _, component in self.components.items():
            component.update(dt, self)

    def render(self, screen, camera):
        # type: (any, Camera) -> None

        self.components[Graphics].render(screen, camera, self)
