class Component:
    """
    Base class for all components that can be added to entities
    """

    def __init__(self):
        pass

    def update(self, dt, owner):
        from entity.entity import Entity
        # type: (float, Entity) -> None
        pass
