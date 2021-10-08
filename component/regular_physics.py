from entity.entity import Entity
from .physics import Physics
from .position import Vector


class RegularPhysics(Physics):
    def __init__(self, velocity=Vector(0,0), accel=Vector(0,0)):
        # type: (Vector, Vector) -> None

        self.velocity = velocity
        self.acceleration = accel

    def update(self, dt, owner):
        # type: (float, Entity) -> None

        adt = self.acceleration * dt # cache this to reuse

        # d = Vi * t + 1/2 * a * t^2
        owner.position += self.velocity * dt + 0.5 * adt * dt

        # Vf = Vi + a * t
        self.velocity += adt
