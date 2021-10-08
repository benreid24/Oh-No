from typing import List

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
        self.graphic = graphic
        self.alive = True
        self.components: List[Component] = []
        self.controller = Controller()
        self.physics = Physics()

    def update(self, dt):
        # type: (float) -> None

        self.controller.update(dt, self)
        self.physics.update(dt, self)
        self.graphic.update(dt, self)

        for component in self.components:
            component.update(dt, self)

    def render(self, screen, camera):
        # type: (any, Camera) -> None

        self.graphic.render(screen, camera, self)
