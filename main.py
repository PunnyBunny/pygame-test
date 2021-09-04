from typing import Tuple

import pygame

WIN_WIDTH = 1000
WIN_HEIGHT = 600


class Background(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, location: Tuple[int, int]):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = location

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, dx, dy):
        self.rect.left += dx
        if self.rect.left > self.width:
            self.rect.left -= self.width * 2
        elif self.rect.right < 0:
            self.rect.left += self.width * 2
        self.rect.top += dy
        if self.rect.top > self.height:
            self.rect.top -= self.height * 2
        elif self.rect.bottom < 0:
            self.rect.top += self.height * 2


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    background_image = pygame.image.load('background.jpg')
    background_image = pygame.transform.scale(background_image, (WIN_WIDTH, WIN_HEIGHT))
    backgrounds = pygame.sprite.Group(
        Background(background_image, (0, 0)),
        Background(background_image, (background_image.get_width(), 0))
    )
    clock = pygame.time.Clock()

    speed = 5
    cur_speed = 0

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    cur_speed -= speed
                elif e.key == pygame.K_RIGHT:
                    cur_speed += speed
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    cur_speed += speed
                elif e.key == pygame.K_RIGHT:
                    cur_speed -= speed
            elif e.type == pygame.QUIT:
                running = False
        backgrounds.update(cur_speed, 0)
        backgrounds.draw(screen)
        pygame.display.flip()

        clock.tick(30)



if __name__ == '__main__':
    main()
