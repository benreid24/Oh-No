from .component import Component


class Physics(Component):
    """
    Base class for all physics that can be added to entities
    """

    def __init__(self):
        super().__init__()

    def update(self, dt, owner):
        from entity.entity import Entity
        # type: (float, Entity) -> None

        return super().update(dt, owner)

    def set_acceleration(self, amount, direction):
        # type: (float, float) -> None
        pass
