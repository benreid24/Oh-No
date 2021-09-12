from camera import Camera
import math

class Entity:
    def __init__(self, position, angle = 180, accel_rate = 1, rotate_rate = .5, graphic):
        self.position = position
        self.graphic = graphic
        self.angle = angle
        self.velocity_x = 0
        self.velocity_y = 0
        self.accel_rate = accel_rate
        self.rotate_rate = rotate_rate
        self.accel = False
        self.rotate_clockwise = False
        self.rotate_counterclockwise = False

    def update(self, dt):
        pass
    
    def update_physics(self, dt):
        self._accelerate(dt)
        self._rotate(dt)
        pass

    def render(self, screen, camera: Camera):
        rect = self.graphic.get_rect(
            topleft=(
                self.position[0] - camera.position[0],
                self.position[1] - camera.position[1]
            )
        )
        screen.blit(self.graphic, rect)

    def _accelerate(self, dt):
        if self.accel == True:
            self.velocity_x += self.accel_rate * dt * cos_angle(self.angle)
            self.velocity_y += self.accel_rate * dt * sin_angle(self.angle)

    def _rotate(self, dt):
        if self.rotate_clockwise == True:
            self.angle = (self.angle + self.rotate_rate * dt ) % 360
        if self.rotate_counterclockwise == True:
            self.angle = (self.angle - self.rotate_rate * dt ) % 360