class Stage:
    def __init__(self) -> None:
        self.size = (2500, 2500)
        self.spawned_bases = []  # Bases spawned

    def initialize(self, world):
        # TODO - spawn starbases and other entities specific to this stage
        raise Exception('Stage does not spawn its entities')

    def active(self):
        for base in self.spawned_bases:
            if base.alive:
                return True
        return False
