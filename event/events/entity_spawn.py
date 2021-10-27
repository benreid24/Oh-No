from entity.entity import Entity

class EntitySpawnEvent:
    def __init__(self, entity):
        # type: (Entity) -> None
        self.entity = entity
