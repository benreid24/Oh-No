from typing import Tuple
from component.minimap import ShowsOnMinimap

from constants import DEFAULT_VIEWPORT
from component.position import Position, Vector


class Camera:
    """
    Defines a render transform that maps a viewport in world coordinates to a region on the screen
    """
    def __init__(self, entity=None, size=Vector(DEFAULT_VIEWPORT[0], DEFAULT_VIEWPORT[1]), render_region=None, minimap=False):
        from entity.entity import Entity
        # type: (Entity, Vector, Tuple[float, float, float, float]) -> None

        self.minimap = minimap
        self.position = Position(0, 0)
        self.entity = entity # type: Entity
        self.size = size # type: Vector
        self.render_region = render_region if render_region else (0, 0, self.size.x, self.size.y)
        self._update_scale()

    def _update_scale(self):
        self.scale = Vector(self.render_region[2] / self.size.x, self.render_region[3] / self.size.y)
        self.entity_scale = self.scale

    def _entity_scale(self, entity):
        return entity.components[ShowsOnMinimap].scale if self.minimap and ShowsOnMinimap in entity.components else 1

    def update(self, dt):
        # type: (float) -> None
        if self.entity:
            self.position = self.entity.position - self.size / 2

    def set_render_region(self, region):
        # type: (Tuple[float, float, float, float]) -> None
        self.render_region = region
        self._update_scale()

    def set_entity_scale(self, scale):
        # type: (Vector) -> None
        self.entity_scale = scale

    def transform_point(self, pos):
        # type: (Position) -> Tuple[float, float]
        return (
            (pos.x - self.position.x) * self.scale.x + self.render_region[0],
            (pos.y - self.position.y) * self.scale.y + self.render_region[1]
        )

    def transform_entity_scalar(self, entity, value):
        from entity.entity import Entity
        # type: (Entity, float) -> float
        return value * self.entity_scale.x * self._entity_scale(entity)

    def transform_entity_size_tuple(self, entity, tup):
        from entity.entity import Entity
        # type: (Entity, Tuple[float, float]) -> Tuple[int, int]
        return (
            int(tup[0] * self.entity_scale.x * self._entity_scale(entity)),
            int(tup[1] * self.entity_scale.y * self._entity_scale(entity))
        )

    def get_visible_area(self):
        # type: () -> Tuple[float, float, float, float]
        return (self.position.x, self.position.y, self.size.x, self.size.y)
