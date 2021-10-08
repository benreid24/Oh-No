import math

from .physics import Physics
from entity.entity import Entity
from .collidable import Collidable
from constants import G


class OrbitalPhysics(Physics):
    def __init__(self, parent, owner, clockwise=True):
        # type: (Entity, Entity, bool) -> None

        super().__init__()
        if Collidable not in parent.components:
            raise Exception('Parent entity of orbit must be Collidable')

        self.parent = parent
        dx = parent.position.x - owner.position.x
        dy = parent.position.y - owner.position.y
        self.radius = math.sqrt(dx*dx + dy*dy)
        self.phase = math.atan2(dy, dx)
        self._direction = -1 if clockwise else 1

        circumfrence = 2 * math.pi * self.radius
        orbital_velocity = math.sqrt(parent.components[Collidable].mass * G / self.radius)
        period = circumfrence / orbital_velocity
        self.angular_velocity = 2 * math.pi / period

    def update(self, dt, owner):
        # type: (float, Entity) -> None
        self.phase += dt * self.angular_velocity * self._direction
        owner.position.x = self.parent.position.x + math.cos(self.phase) * self.radius
        owner.position.y = self.parent.position.y + math.sin(self.phase) * self.radius
        