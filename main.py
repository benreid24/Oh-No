import sys

import pygame

from constants import WINDOW_RESOLUTION
from world.world import World


def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_RESOLUTION)
    pygame.display.set_caption('Oh no')

    world = World()
    world.generate_world()
    world.spawn_player()
    
    clock = pygame.time.Clock()
    ms = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        world.update(ms / 1000)

        world.render(screen)
        ms = clock.tick(60)  # 60 fps


if __name__ == '__main__':
    main()
