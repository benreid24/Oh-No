import math
from enum import Enum

from component.position import Vector
from .component import Component
from entity.entity import Entity

class Collidable(Component):
    class BoundType(Enum):
        Box = 1
        Circle = 2

    def __init__(self, type, mass=1, width=0, height=0, radius=0):
        # type: (Collidable.BoundType, float, float, float, float) -> None

        self.mass = mass
        self.center = Vector(0, 0)
        self.type = type
        self.width = width
        self.height = height
        self.radius = radius

    def update(self, dt, owner):
        # type: (float, Entity) -> None
        self.center = owner.position

    def is_colliding(self, other):
        # type: (Collidable) -> bool
        
        def box_overlap(l, r):
            # type: (Collidable, Collidable) -> bool
            # TODO - this assumes that the rects are aligned. We need to axis align them first
            dx = l.center.x - r.center.x
            dy = l.center.y - r.center.y
            hws = l.width * 0.5 + r.width * 0.5
            hhs = l.height * 0.5 + r.height * 0.5
            return abs(dx) < hws and abs(dy) < hhs

        def circle_overlap(l, r):
            # type: (Collidable, Collidable) -> bool
            dx = l.center.x - r.center.x
            dy = l.center.y - r.center.y
            rs = l.radius + r.radius
            return dx*dx + dy*dy < rs*rs

        def box_circle_overlap(box, circle):
            # type: (Collidable, Collidable) -> bool
            # TODO - this is actually pretty hard
            pass

        if self.type == Collidable.BoundType.Box:
            if other.type == Collidable.BoundType.Box:
                return box_overlap(self, other)
            return box_circle_overlap(self, other)
        if other.type == Collidable.BoundType.Box:
            return box_circle_overlap(other, self)
        return circle_overlap(self, other)

    def get_collision_angle(self, other):
        # type: (Collidable) -> float
        return math.atan2(self.center.y - other.center.y, self.center.x - other.center.x) * 180 / math.pi
