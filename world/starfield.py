from typing import Tuple, List
import math
from random import uniform, choice

import pygame

from constants import WHITE
from camera import Camera
from component.position import Vector

EXTRA_SPACE = 100


class Star:
    def __init__(self, pos, radius, rad_var=0, rad_freq=2):
        # type: (Vector, float, float, float) -> None
        self.position = pos
        self.radius = radius
        self.rad_var = rad_var
        self.rad_freq = rad_freq
        self.t = 0

    def update(self, dt):
        self.t += dt

    def render(self, surface, camera):
        # type: (any, Camera) -> None
        pygame.draw.circle(
            surface,
            WHITE,
            camera.transform(self.position),
            max(self.radius + self.rad_var * math.cos(self.t * self.rad_freq), 1)
        )

class Starfield:
    @staticmethod
    def _make_star(region):
        # type: (Tuple[float, float, float, float]) -> Star
        return Star(
            Vector(
                uniform(region[0]-EXTRA_SPACE, region[0] + region[2] + EXTRA_SPACE),
                uniform(region[1]-EXTRA_SPACE, region[1] + region[3] + EXTRA_SPACE)
            ),
            uniform(0.5, 3),
            uniform(0, 1),
            uniform(1, 8)
        )

    def __init__(self, max_stars, region):
        # type: (int, Tuple[float, float, float, float]) -> None
        self.stars = [Starfield._make_star(region) for _ in range(max_stars)]
        self.region = (
            region[0] - EXTRA_SPACE,
            region[1] - EXTRA_SPACE,
            region[2] + EXTRA_SPACE * 2,
            region[3] + EXTRA_SPACE * 2
        )
        self.spawn_regions = Starfield._make_regions(region)

    def update(self, dt):
        # type: (float) -> None

        for i in range(len(self.stars)):
            self.stars[i].update(dt)
            if not self.stars[i].position.within(self.region):
                self.stars[i] = Starfield._make_star(choice(self.spawn_regions))

    def render(self, surface, camera):
        # type: (any, Camera) -> None
        r = camera.get_area()
        self.region = (
            r[0] - EXTRA_SPACE,
            r[1] - EXTRA_SPACE,
            r[2] + EXTRA_SPACE * 2,
            r[3] + EXTRA_SPACE * 2
        )
        self.spawn_regions = Starfield._make_regions(r)
        for star in self.stars:
            star.render(surface, camera)

    @staticmethod
    def _make_regions(region):
        # type: (Tuple[float, float, float, float]) -> List[Tuple[float, float, float, float]]
        return [
            (
                region[0] - EXTRA_SPACE,
                region[1] - EXTRA_SPACE,
                region[2] + EXTRA_SPACE * 2,
                EXTRA_SPACE
            ),
            (
                region[0] + region[2],
                region[1],
                EXTRA_SPACE,
                region[3] + EXTRA_SPACE
            ),
            (
                region[0] - EXTRA_SPACE,
                region[1],
                EXTRA_SPACE,
                region[3] + EXTRA_SPACE
            ),
            (
                region[0],
                region[1] + region[3],
                region[2],
                EXTRA_SPACE
            )
        ]
