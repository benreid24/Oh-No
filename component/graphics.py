from .component import Component
from camera import Camera


class Graphics(Component):
    """
    Base class for all graphics for entities
    """

    def __init__(self) -> None:
        super().__init__()

    def update(self, dt, owner):
        from entity.entity import Entity
        # type: (float, Entity) -> None
        return super().update(dt, owner)

    def render(self, screen, camera, owner):
        from entity.entity import Entity
        # type: (any, Camera, Entity) -> None
        pass
    