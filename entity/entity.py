from camera import Camera
from component.position import Position

class Entity:
    def __init__(self, position: Position, graphic): # TODO - make an animation class
        self.position = position
        self.graphic = graphic
        self.alive = True

    def update(self, dt: float):
        pass

    def render(self, screen, camera: Camera):
        rect = self.graphic.get_rect(
            topleft=(
                self.position.x - camera.position.y,
                self.position.y - camera.position.y
            )
        )
        screen.blit(self.graphic, rect)
