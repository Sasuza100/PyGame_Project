import pygame

pygame.init()
screen = pygame.display.set_mode((840, 640))
screen_rect = screen.get_rect()

l_player = pygame.Rect(10, 10, 10, 250)
r_player = pygame.Rect(820, 10, 10, 250)
ball = pygame.circle

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: l_player.move_ip(0, -1)
    if keys[pygame.K_s]: l_player.move_ip(0, 1)
    l_player.clamp_ip(screen_rect)

    if keys[pygame.K_UP]: r_player.move_ip(0, -1)
    if keys[pygame.K_DOWN]: r_player.move_ip(0, 1)
    r_player.clamp_ip(screen_rect)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), l_player)
    pygame.draw.rect(screen, (255, 255, 255), r_player)
    pygame.display.flip()
