import os
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((840, 640))


def terminate():
    pygame.quit()
    sys.exit()


def draw_text(screen):
    intro_text = ["PONG", "",
                  "Левый игрок использует W и S для передвижения и Q и A для бафов",
                  "Правый игрок использует стрелки для передвижения и P и L для бафов",
                  "При достижении одним из игроков результата в 30 очков игра будет завершена",
                  "Настройте скорость стрелками", "Для начала игры нажмите пробел"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (840, 640))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def draw_speed(screen, speed):
    intro_text = f"Текущая скорость {speed}"

    font = pygame.font.Font(None, 30)
    text_coord = 300
    string_rendered = font.render(intro_text, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 10
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)


def start_screen():
    """Создание экрана"""
    clock = pygame.time.Clock()
    speed = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed += 1
                elif event.key == pygame.K_DOWN:
                    speed -= 1
                elif event.key == pygame.K_SPACE:
                    return speed
        pygame.Color("black")
        draw_text(screen)
        draw_speed(screen, speed)
        pygame.display.flip()
        clock.tick(50)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image
