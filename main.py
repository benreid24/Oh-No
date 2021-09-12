import sys

import pygame

BLACK = 0, 0, 0


def main():
    pygame.init()

    resolution = 800, 600
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption('Oh no')
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # update game logic

        screen.fill(BLACK)
        # render scene
        pygame.display.flip()

        # ensure fps
        clock.tick(60)  # 60 fps


if __name__ == '__main__':
    main()
