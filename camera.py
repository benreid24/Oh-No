from constants import RESOLUTION


class Camera:
    def __init__(self) -> None:
        self.position = 0, 0
        self.entity = None

    def update(self, dt):
        if self.entity:
            self.position[0] = self.entity.get_position()[0] - RESOLUTION[0] // 2
            self.position[1] = self.entity.get_position()[1] - RESOLUTION[1] // 2
