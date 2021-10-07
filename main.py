import sys

import pygame

from constants import RESOLUTION
from world.world import World
import math

def main():
    pygame.init()

    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption('Oh no')
    clock = pygame.time.Clock()
    ms = 0

    world = World()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if not world.update(ms / 1000):
            # TODO - victory screen
            break
        world.render(screen)
        ms = clock.tick(60)  # 60 fps

if __name__ == '__main__':
    main()
