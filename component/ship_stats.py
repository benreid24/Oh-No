from .component import Component


class ShipStats(Component):
    """
    Contains stats for a ship
    """

    def __init__(self, acceleration=10, max_vel=300, rotate_vel=120):
        # type: (float, float, float) -> None
        
        self.acceleration = acceleration
        self.max_vel = max_vel
        self.rotate_vel = rotate_vel
