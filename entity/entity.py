from camera import Camera
import math
from main.py

class Entity:
    def __init__(self, position, angle = 180, graphic):
        self.position = position
        self.graphic = graphic
        self.angle = angle
        self.velocity_x = 0
        self.velocity_y = 0
        self.accel_x = 0
        self.accel_y = 0
        
    def update(self, dt):
        pass
    
    def update_physics(self, rotate_rate, accel_rate, dt):
        self._position(self, dt)

    def render(self, screen, camera: Camera):
        rect = self.graphic.get_rect(
            topleft=(
                self.position[0] - camera.position[0],
                self.position[1] - camera.position[1]
            )
        )
        screen.blit(self.graphic, rect)

    def _position(self, dt):
        pos_x += self.velocity_x * dt + .5 * self.accel_x * dt**2
        pos_y += self.velocity_y * dt + .5 * self.accel_y * dt**2
        self.position = (pos_x ,pos_y )

    def _accelerate(self, dt):
        self.accel_x = accel_rate * dt * cos_angle(self.angle)
        self.accel_y = accel_rate * dt * sin_angle(self.angle)
        self.velocity_x += self.accel_x
        self.velocity_y += self.accel_y

    def _rotate(self, rotate_rate, dt):
        self.angle = (self.angle + rotate_rate * dt ) % 360