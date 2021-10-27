from .component import Component
from .graphics import Graphics


class ShowsOnMinimap(Component):
    """
    Empty component. It's presence causes an entity to be rendered on the minimap
    """
    def __init__(self, scale=1, render_override=None):
        # type: (float, Graphics) -> None
        super().__init__()
        self.scale = scale
        self.render_override = render_override

    def update(self, dt, owner):
        if self.render_override:
            self.render_override.update(dt, owner)
