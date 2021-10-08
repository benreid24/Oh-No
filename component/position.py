class Vector:
    def __init__(self, x, y):
        # type: (float, float) -> None
        self.x = x
        self.y = y

    def __add__(self, vec):
        # type: (Vector) -> Vector
        return Vector(self.x + vec.x, self.y + vec.y)


    def __mul__(self, s):
        # type: (float) -> Vector
        return Vector(self.x * s, self.y * s)


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
