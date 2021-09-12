from constants import RESOLUTION


class Camera:
    def __init__(self, entity=None) -> None:
        self.position = 0, 0
        self.entity = entity

    def update(self, dt):
        if self.entity:
            self.position = (
                self.entity.position[0] - RESOLUTION[0] // 2,
                self.entity.position[1] - RESOLUTION[1] // 2
            )
