from world.stage import Stage
from entity.starbases.basic import BasicStarbase


class Stage1(Stage):
    def __init__(self) -> None:
        super().__init__()

    def initialize(self, world):
        self.spawned_bases = [
            BasicStarbase((100, 100)),
            BasicStarbase((100, 500)),
            BasicStarbase((500, 100))
        ]
        for base in self.spawned_bases:
            world.spawn_entity(base)
