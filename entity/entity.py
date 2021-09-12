from camera import Camera

class Entity:
    def __init__(self, position, graphic):
        self.position = position
        self.graphic = graphic
        self.alive = True

    def update(self, dt):
        pass

    def render(self, screen, camera: Camera):
        rect = self.graphic.get_rect(
            topleft=(
                self.position[0] - camera.position[0],
                self.position[1] - camera.position[1]
            )
        )
        screen.blit(self.graphic, rect)
