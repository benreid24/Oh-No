import math
from enum import Enum

from component.position import Vector
from .component import Component
from entity.entity import Entity


class BoundingArea:
    class BoundType(Enum):
        Box = 1
        Circle = 2

    def __init__(self, type, width=0, height=0, radius=0):
        # type: (BoundingArea.BoundType, float, float, float) -> None

        self.center = Vector(0, 0)
        self.type = type
        self.width = width
        self.height = height
        self.radius = radius

    def is_colliding(self, other):
        # type: (BoundingArea) -> bool
        
        def box_overlap(l, r):
            # type: (BoundingArea, BoundingArea) -> bool
            # TODO - this assumes that the rects are aligned. We need to axis align them first
            dx = l.center.x - r.center.x
            dy = l.center.y - r.center.y
            hws = l.width * 0.5 + r.width * 0.5
            hhs = l.height * 0.5 + r.height * 0.5
            return abs(dx) < hws and abs(dy) < hhs

        def circle_overlap(l, r):
            # type: (BoundingArea, BoundingArea) -> bool
            dx = l.center.x - r.center.x
            dy = l.center.y - r.center.y
            rs = l.radius + r.radius
            return dx*dx + dy*dy < rs*rs

        def box_circle_overlap(box, circle):
            # type: (BoundingArea, BoundingArea) -> bool
            # TODO - this is actually pretty hard
            pass

        if self.type == BoundingArea.BoundType.Box:
            if other.type == BoundingArea.BoundType.Box:
                return box_overlap(self, other)
            return box_circle_overlap(self, other)
        if other.type == BoundingArea.BoundType.Box:
            return box_circle_overlap(other, self)
        return circle_overlap(self, other)

    def get_collision_angle(self, other):
        # type: (BoundingArea) -> float
        return math.atan2(self.center.y - other.center.y, self.center.x - other.center.x) * 180 / math.pi


class Collidable(Component):
    def __init__(self, bounds, mass=1):
        # type: (BoundingArea, float) -> None
        self.bounds = bounds
        self.mass = mass

    def update(self, dt, owner):
        # type: (float, Entity) -> None
        self.bounds.center = owner.position

    def is_colliding(self, other):
        # type: (Collidable) -> bool
        return self.bounds.is_colliding(other.bounds)
