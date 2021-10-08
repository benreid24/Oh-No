from .component import Component
from.physics import Physics
from .ship_stats import ShipStats


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

    @staticmethod
    def accelerate(entity):
        from entity.entity import Entity
        # type: (Entity) -> None
        
        physics: Physics = entity.components.get(Physics, None)
        if not physics:
            print('Entity is missing physics but is being controlled')
            return

        stats: ShipStats = entity.components.get(ShipStats, None)
        if not stats:
            print('Entity is missing stats but is being controlled')
            return

        physics.set_acceleration(stats.acceleration, entity.position.angle)

    @staticmethod
    def freeze(entity):
        from entity.entity import Entity
        # type: (Entity) -> None

        physics: Physics = entity.components.get(Physics, None)
        if not physics:
            print('Entity is missing physics but is being controlled')
            return

        physics.set_acceleration(0, 0)

    @staticmethod
    def rotate(entity, dt, left):
        from entity.entity import Entity
        # type: (Entity, float, bool)

        stats: ShipStats = entity.components.get(ShipStats, None)
        if not stats:
            print('Entity is missing stats but is being controlled')
            return

        dir = -1 if left else 1
        entity.position.angle += stats.rotate_vel * dt * dir
