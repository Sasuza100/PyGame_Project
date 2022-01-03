import pygame
import random
import pygame

pygame.init()

l_player = pygame.Rect(10, 10, 10, 250)
r_player = pygame.Rect(820, 10, 10, 250)


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


all_sprites = pygame.sprite.Group()

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

size = width, height = 840, 640
screen = pygame.display.set_mode(size)
screen_rect = screen.get_rect()
# horizontal
Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border()


for i in range(1):
    Ball(20, 100, 100)

clock = pygame.time.Clock()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: l_player.move_ip(0, -5)
    if keys[pygame.K_s]: l_player.move_ip(0, 5)
    l_player.clamp_ip(screen_rect)

    if keys[pygame.K_UP]: r_player.move_ip(0, -5)
    if keys[pygame.K_DOWN]: r_player.move_ip(0, 5)
    r_player.clamp_ip(screen_rect)

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(50)
    pygame.draw.rect(screen, (255, 255, 255), l_player)
    pygame.draw.rect(screen, (255, 255, 255), r_player)
    pygame.display.flip()
