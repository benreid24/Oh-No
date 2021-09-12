import sys

import pygame

from constants import BLACK, RESOLUTION
from entity.entity import Entity
from camera import Camera


def main():
    pygame.init()

    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption('Oh no')
    clock = pygame.time.Clock()

    test_entity = Entity((300, 300), pygame.image.load('resources/test.png'))
    camera = Camera()
    ms = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # update game logic
        camera.update(ms)

        screen.fill(BLACK)
        
        # render scene
        test_entity.render(screen, camera)

        pygame.display.flip()

        # ensure fps
        ms = clock.tick(60)  # 60 fps


if __name__ == '__main__':
    main()
