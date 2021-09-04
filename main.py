import time

import pygame

WIN_WIDTH = 1000
WIN_HEIGHT = 600
PLAYER_SIZE = 50


class Background(pygame.sprite.Sprite):
    def __init__(s, image: pygame.Surface, x: int, y: int):
        pygame.sprite.Sprite.__init__(s)

        s.image = image
        s.rect = s.image.get_rect()
        s.rect.topleft = x, y

        s.width = s.image.get_width()
        s.height = s.image.get_height()

    def update(s, dx, dy):
        s.rect.left += dx
        if s.rect.left > s.width:
            s.rect.left -= s.width * 2
        elif s.rect.right < 0:
            s.rect.left += s.width * 2
        s.rect.top += dy
        if s.rect.top > s.height:
            s.rect.top -= s.height * 2
        elif s.rect.bottom < 0:
            s.rect.top += s.height * 2


class Player(pygame.sprite.Sprite):

    def __init__(s, x, y):
        pygame.sprite.Sprite.__init__(s)

        s.image = pygame.surface.Surface((PLAYER_SIZE, PLAYER_SIZE))
        s.image.fill((0,0,0))
        s.rect = s.image.get_rect()
        s.rect.topleft = x, y

        s.a = 0
        s.u = 0
        s.t = 0

    def jump(s, t):
        s.a = 20
        s.t = t
        s.u = -10

    def update(s, t: float, dx: int):
        t = t - s.t
        s.rect.top += int(s.u + s.a * t)
        if s.rect.bottom > WIN_HEIGHT:
            s.rect.bottom = WIN_HEIGHT
            s.a = 0
            s.u = 0
        s.rect.left += dx
        if s.rect.left < 0:
            s.rect.left = 0
        if s.rect.right > WIN_WIDTH:
            s.rect.right = WIN_WIDTH


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    background_image = pygame.image.load('background.jpg')
    background_image = pygame.transform.scale(background_image, (WIN_WIDTH, WIN_HEIGHT))
    backgrounds = pygame.sprite.Group(
        Background(background_image, 0, 0),
        Background(background_image, background_image.get_width(), 0)
    )
    clock = pygame.time.Clock()

    speed = 10
    cur_speed = 0

    player = Player(WIN_WIDTH // 2 - PLAYER_SIZE // 2, WIN_HEIGHT - PLAYER_SIZE)

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                cur_speed += speed if e.key == pygame.K_LEFT else -speed if e.key == pygame.K_RIGHT else 0
                if e.key == pygame.K_UP:
                    player.jump(time.perf_counter())

            elif e.type == pygame.KEYUP:
                cur_speed -= speed if e.key == pygame.K_LEFT else -speed if e.key == pygame.K_RIGHT else 0

            elif e.type == pygame.QUIT:
                running = False

        backgrounds.update(cur_speed, 0)
        player.update(time.perf_counter(), 0)
        backgrounds.draw(screen)
        screen.blit(player.image, player.rect)
        pygame.display.flip()

        clock.tick(60)


if __name__ == '__main__':
    main()
