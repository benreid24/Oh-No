from camera import Camera
from helpers import cos_angle, sin_angle

class Entity:
    def __init__(self, position, angle, graphic):
        self.position = [position[0], position[1]]
        self.graphic = graphic
        self.angle = angle
        self.velocity_x = 0
        self.velocity_y = 0
        self.accel_x = 0
        self.accel_y = 0

    def update(self, dt):
        pass

    def update_physics(self, rotate_rate, accel_rate, dt):
        self._position(dt)
        self.velocity_x += self.accel_x * dt
        self.velocity_y += self.accel_y * dt

    def render(self, screen, camera: Camera):
        rect = self.graphic.get_rect(
            topleft=(
                self.position[0] - camera.position[0],
                self.position[1] - camera.position[1]
            )
        )
        screen.blit(self.graphic, rect)

    def _position(self, dt):
        pos_x = self.velocity_x * dt + .5 * self.accel_x * dt**2
        pos_y = self.velocity_y * dt + .5 * self.accel_y * dt**2
        self.position[0] += pos_x
        self.position[1] += pos_y

    def _accelerate(self, accel_rate, dt):
        self.accel_x = accel_rate * dt * cos_angle(self.angle)
        self.accel_y = accel_rate * dt * sin_angle(self.angle)

    def _rotate(self, rotate_rate, dt):
        self.angle = (self.angle + rotate_rate * dt ) % 360