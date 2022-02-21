from start_screen import *
from PIL import Image

pygame.init()

l_player = pygame.Rect(10, 10, 10, 180)
r_player = pygame.Rect(820, 10, 10, 180)

x_v = start_screen()


class Ball(pygame.sprite.Sprite):

    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = x_v
        self.vy = x_v + 1
        self.old_vx = self.vx
        self.old_vy = self.vy
        self.r_player_points = 0
        self.l_player_points = 0
        self.l_player_count = 0
        self.r_player_count = 0
        self.time_count = 0.0001

    def update(self):
        global fps_count
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
        self.time_count = fps_count / 50
        if self.r_player_points >= 3 and keys[pygame.K_p]:  # Если у игрока есть 3 очка, то он может использовать ускорение(на 3 секунды)
            self.r_player_points -= 3
            self.time_count = 0
            fps_count = 0
            self.vy = self.vy * 1.7
            self.vx = self.vx * 1.7
            if self.time_count == 3:
                self.vy = self.vy / 1.7
                self.vx = self.vx / 1.7

        if self.l_player_points >= 3 and keys[pygame.K_q]:
            self.l_player_points -= 3
            self.time_count = 0
            fps_count = 0
            self.vy = self.vy * 1.7
            self.vx = self.vx * 1.7
            if self.time_count == 3:
                self.vy = self.vy / 1.7
                self.vx = self.vx / 1.7

        print(self.vx, self.vy)

        if self.rect.centerx > 840:
            self.l_player_points += 0.5
            self.l_player_count += 1
            self.rect.centerx = 420
            self.rect.centery = 320
            self.vy = -self.vy

        if self.rect.centerx < 0:
            self.r_player_count += 1
            self.r_player_points += 0.5
            self.rect.centerx = 420
            self.rect.centery = 320
            self.vy = -self.vy

        font = pygame.font.Font(None, 50)
        text = font.render(f'{str(self.l_player_count)} : {str(self.r_player_count)}', True, (255, 255, 255))
        text_x = width // 2 - text.get_width() // 2
        screen.blit(text, (text_x, 20))

        point_l = font.render(f'{str(self.l_player_points)}', True, (0, 103, 126))
        point_l_coord = width // 13 - point_l.get_width() // 13
        screen.blit(point_l, (point_l_coord, 20))
        point_r = font.render(f'{str(self.r_player_points)}', True, (0, 168, 107))
        point_r_coord = width // 1.08 - point_r.get_width() // 1.08
        screen.blit(point_r, (point_r_coord, 20))


class Border(pygame.sprite.Sprite):

    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.kill()
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

for i in range(1):
    Ball(20, 100, 100)

clock = pygame.time.Clock()

fps_count = 0

run = True
while run:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        l_player.move_ip(0, -5)
    if keys[pygame.K_s]:
        l_player.move_ip(0, 5)
    l_player.clamp_ip(screen_rect)
    if keys[pygame.K_UP]:
        r_player.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        r_player.move_ip(0, 5)
    r_player.clamp_ip(screen_rect)
    horizontal_borders = None
    vertical_borders = None
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    Border(20, l_player.top, 20, l_player.top + 180)
    Border(820, r_player.top, 820, r_player.top + 180)
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)

    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(50)
    pygame.draw.rect(screen, (255, 255, 255), l_player)
    pygame.draw.rect(screen, (255, 255, 255), r_player)
    fps_count += 1
    pygame.display.flip()
