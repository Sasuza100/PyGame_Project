import pygame.transform
from start_screen import *
from add_imgs import *

pygame.init()
sound = pygame.mixer.Sound("data/wow.wav")
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
        self.r_player_points = 0
        self.l_player_points = 0
        self.l_player_count = 0
        self.r_player_count = 0
        self.time_count = 0.0001
        self.r_b_flag = False
        self.l_b_flag = False
        self.r_flag = False
        self.l_flag = False

    def update(self):
        global fps_count, fps_count2, r_rak_up, r_rak_down, l_rak_up, l_rak_down, run
        self.rect = self.rect.move(self.vx, self.vy)

        # отталкивание от стен
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
            sound.play()
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
            sound.play()

        # баф для шара со стороны левого игрока
        self.time_count = fps_count / 50
        if self.time_count >= 3 and self.r_player_points >= 3 and keys[pygame.K_p]:  # Если у игрока есть 3 очка, то он может использовать ускорение для шара(на 3 секунды)
            self.r_player_points -= 3
            self.time_count = 0
            fps_count = 0
            if self.vy <= 50:
                self.vy = self.vy * 1.7
            if self.vx <= 50:
                self.vx = self.vx * 1.7
            self.r_b_flag = True
        if self.time_count >= 3 and self.r_b_flag:
            self.vy = self.vy / 1.7
            self.vx = self.vx / 1.7
            self.r_b_flag = False

        # баф для шара со стороны правого игрока
        if self.time_count >= 3 and self.l_player_points >= 3 and keys[pygame.K_q]:
            self.l_player_points -= 3
            self.time_count = 0
            fps_count = 0
            if self.vy <= 50:
                self.vy = self.vy * 1.7
            if self.vx <= 50:
                self.vx = self.vx * 1.7
            self.l_b_flag = True
        if self.time_count >= 3 and self.l_b_flag:
            self.vy = self.vy / 1.7
            self.vx = self.vx / 1.7
            self.l_b_flag = False



        self.time_count2 = fps_count2 / 50
        # баф для ракетки со стороны правого игрока
        if self.time_count >= 3 and self.r_player_points >= 1.5 and keys[pygame.K_l]:
            self.r_player_points -= 1.5
            self.time_count2 = 0
            fps_count2 = 0
            r_rak_up = -10
            r_rak_down = 10
            self.r_flag = True

        if self.time_count2 >= 3 and self.r_flag:
            r_rak_up = -5
            r_rak_down = 5
            self.r_flag = False
        # баф для ракетки со стороны левого игрока
        if self.time_count >= 3 and self.l_player_points >= 1.5 and keys[pygame.K_a]:
            self.l_player_points -= 1.5
            self.time_count2 = 0
            fps_count2 = 0
            l_rak_up = -10
            l_rak_down = 10
            self.l_flag = True
        if self.time_count2 >= 3 and self.l_flag:
            l_rak_up = -5
            l_rak_down = 5
            self.l_flag = False

        # реализация голов на правом краю
        if self.rect.centerx > 840:
            self.l_player_points += 0.5
            self.l_player_count += 1
            if (self.l_player_count + self.r_player_count) % 5 == 0 and self.l_player_count != 0 and self.r_player_count != 0:
                if self.vx <= 50:
                    self.vx = self.vx * 1.2
            self.rect.centerx = 420
            self.rect.centery = 320
            self.vy = -self.vy
        # реализация голов на левом краю
        if self.rect.centerx < 0:
            self.r_player_count += 1
            self.r_player_points += 0.5
            if (self.l_player_count + self.r_player_count) % 5 == 0 and self.l_player_count != 0 and self.r_player_count != 0:
                if self.vx <= 50:
                    self.vx = self.vx * 1.2
            self.rect.centerx = 420
            self.rect.centery = 320
            self.vy = -self.vy

        # вывод счёта
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

        # отрисовка иконок покупки
        if self.r_player_points < 3:
            buff_img_rocket_bw_r()
        else:
            buff_img_rocket_r()
        if self.r_player_points < 1.5:
            buff_img_racket_bw_r()
        else:
            buff_img_racket_r()

        if self.l_player_points < 3:
            buff_img_rocket_bw_l()
        else:
            buff_img_rocket_l()
        if self.l_player_points < 1.5:
            buff_img_racket_bw_l()
        else:
            buff_img_racket_l()
        if self.l_player_count >= 30:
            terminate()

        if self.r_player_count >= 30:
            terminate()




# класс для добавления стен, взят из уроков
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

# спавним шар (дальше можно сделать больше)
for i in range(1):
    Ball(20, 100, 100)

clock = pygame.time.Clock()

fps_count = 0
fps_count2 = 0
l_rak_up = -5
l_rak_down = 5
r_rak_up = -5
r_rak_down = 5
run = True
if __name__ == '__main__':
    while run:

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        # двигаем ракетки
        if keys[pygame.K_w]:
            l_player.move_ip(0, l_rak_up)
        if keys[pygame.K_s]:
            l_player.move_ip(0, l_rak_down)
        l_player.clamp_ip(screen_rect)
        if keys[pygame.K_UP]:
            r_player.move_ip(0, r_rak_up)
        if keys[pygame.K_DOWN]:
            r_player.move_ip(0, r_rak_down)
        r_player.clamp_ip(screen_rect)
        # стены тоже
        horizontal_borders = None
        vertical_borders = None
        horizontal_borders = pygame.sprite.Group()
        vertical_borders = pygame.sprite.Group()
        Border(20, l_player.top, 20, l_player.top + 180)
        Border(820, r_player.top, 820, r_player.top + 180)
        Border(5, 5, width - 5, 5)
        Border(5, height - 5, width - 5, height - 5)
        # отрисовывем всё
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(50)
        pygame.draw.rect(screen, (255, 255, 255), l_player)
        pygame.draw.rect(screen, (255, 255, 255), r_player)
        fps_count += 1
        fps_count2 += 1
        pygame.display.flip()
