from .component import Component


class Controller(Component):
    """
    Base class for all entity controllers (player, ai, network, etc)
    """

    def __init__(self):
        super().__init__()

    def update(self, dt, owner):
        from entity.entity import Entity
        # type: (float, Entity) -> None

        return super().update(dt, owner)
