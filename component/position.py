from typing import Tuple


class Vector:
    def __init__(self, x, y):
        # type: (float, float) -> None
        self.x = x
        self.y = y

    def within(self, region):
        # type: (Tuple[float, float, float, float]) -> bool
        return (
            self.x >= region[0] and self.x <= region[0] + region[2] and
            self.y >= region[1] and self.y <= region[1] + region[3]
        )

    def mag_sqrd(self):
        return self.x * self.x + self.y * self.y

    def __add__(self, vec):
        # type: (Vector) -> Vector
        return Vector(self.x + vec.x, self.y + vec.y)

    def __mul__(self, s):
        # type: (float) -> Vector
        return Vector(self.x * s, self.y * s)

    def __rmul__(self, s):
        # type: (float) -> Vector
        return Vector(self.x * s, self.y * s)

    def __truediv__(self, s):
        # type: (float) -> Vector
        return Vector(self.x / s, self.y / s)


class Position:
    """
    Cartesian coordinate with an angle
    """

    def __init__(self, x, y, angle=0):
        # type: (float, float, float) -> None
        self.x = x
        self.y = y
        self.angle = angle

    def __add__(self, pos):
        # type: (Vector) -> Position
        return Position(self.x + pos.x, self.y + pos.y, self.angle)

    def __sub__(self, pos):
        # type: (Vector) -> Position
        return Position(self.x - pos.x, self.y - pos.y, self.angle)
