from pygame import *
from start_screen import load_image
size = width, height = 840, 640
screen = display.set_mode(size)


def buff_img_rocket_bw_l():
    buff1_l = image.load('data/rocket_b_w.png')
    buff1_l_scale = transform.scale(buff1_l, (75, 50))
    screen.blit(buff1_l_scale, ((width / 3), 10))


def buff_img_racket_bw_l():
    buff1_l = image.load('data/racket_b_w.png')
    buff1_l_scale = transform.scale(buff1_l, (75, 50))
    screen.blit(buff1_l_scale, ((width / 3.7), 10))


def buff_img_rocket_bw_r():
    buff1_r = image.load('data/rocket_b_w.png')
    buff1_r_scale = transform.scale(buff1_r, (75, 50))
    screen.blit(buff1_r_scale, ((width / 1.75), 10))


def buff_img_racket_bw_r():
    buff1_l = image.load('data/racket_b_w.png')
    buff1_l_scale = transform.scale(buff1_l, (75, 50))
    screen.blit(buff1_l_scale, ((width / 1.58), 10))


def buff_img_rocket_l():
    buff1_l = image.load('data/rocket.png')
    buff1_l_scale = transform.scale(buff1_l, (75, 50))
    screen.blit(buff1_l_scale, ((width / 3), 10))


def buff_img_racket_l():
    buff1_l = image.load('data/racket.png')
    buff1_l_scale = transform.scale(buff1_l, (75, 50))
    screen.blit(buff1_l_scale, ((width / 3.7), 10))


def buff_img_rocket_r():
    buff1_r = image.load('data/rocket.png')
    buff1_r_scale = transform.scale(buff1_r, (75, 50))
    screen.blit(buff1_r_scale, ((width / 1.75), 10))


def buff_img_racket_r():
    buff1_l = image.load('data/racket.png')
    buff1_l_scale = transform.scale(buff1_l, (75, 50))
    screen.blit(buff1_l_scale, ((width / 1.58), 10))