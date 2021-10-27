from .graphics import Graphics


class FlashingGraphic(Graphics):
    def __init__(self, period, underlying):
        # type: (float, Graphics) -> None
        self.period = period
        self.underlying = underlying
        self.t = 0
        self.visible = True

    def update(self, dt, owner):
        self.t += dt
        if self.t >= self.period:
            self.t -= self.period
            self.visible = not self.visible

    def render(self, screen, camera, owner):
        if self.visible:
            self.underlying.render(screen, camera, owner)
