class Position:
    def __init__(self, x: float, y: float, angle: float=0):
        self.x = x
        self.y = y
        self.angle = angle

    def __add__(self, pos):
        return Position(self.x + pos.x, self.y + pos.y, self.angle + pos.angle)
