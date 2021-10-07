from constants import RESOLUTION
from component.position import Position


class Camera:
    # TODO - do we want to support offsets, scaling, or rotating?
    
    def __init__(self, entity=None) -> None:
        self.position = Position(0, 0)
        self.entity = entity

    def update(self, dt: float):
        if self.entity:
            self.position.x = self.entity.position.x - RESOLUTION[0] // 2
            self.position.y = self.entity.position.y - RESOLUTION[1] // 2
