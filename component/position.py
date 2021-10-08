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
        # type: (Position) -> Position
        return Position(self.x + pos.x, self.y + pos.y, self.angle + pos.angle)
