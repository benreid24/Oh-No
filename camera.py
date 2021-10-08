from typing import Tuple

from constants import RESOLUTION
from component.position import Position


class Camera:
    # TODO - do we want to support offsets, scaling, or rotating?
    
    def __init__(self, entity=None):
        from entity.entity import Entity
        # type: (Entity) -> None

        self.position = Position(0, 0)
        self.entity = entity

    def update(self, dt):
        # type: (float) -> None

        if self.entity:
            self.position.x = self.entity.position.x - RESOLUTION[0] // 2
            self.position.y = self.entity.position.y - RESOLUTION[1] // 2

    def transform(self, pos):
        # type: (Position) -> Tuple[float, float]
        return (
            pos.x - self.position.x,
            pos.y - self.position.y
        )

    def get_area(self):
        # type: () -> Tuple[float, float, float, float]
        return (self.position.x, self.position.y, RESOLUTION[0], RESOLUTION[1])
