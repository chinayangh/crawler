# -*- coding: utf-8 -*-

import random, math, pygame
from pygame.locals import *


# 定义 坐标类

def wrap_angle(angle):
    return angle % 360


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x

    x = property(getx, setx)

    def gety(self):
        return self.__y

    def sety(self, y):
        self.__y = y

    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.x) + \
               ",Y:" + "{:.0f}".format(self.y) + "}"


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("orbit demo")
font = pygame.font.Font(None, 60)
space = pygame.image.load("space2.jpg").convert()
planet = pygame.image.load("planet2.png").convert_alpha()
ship = pygame.image.load("me5.png").convert_alpha()
s_width, s_height = ship.get_size()
width, height = planet.get_size()
ship = pygame.transform.smoothscale(ship, (s_width // 3, s_height // 3))
pos = Point(0, 0)
old_pos = Point(0, 0)
angle = 0.0
# angle = wrap_angle(angle -0.1)
radius = 250
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
    # background
    screen.blit(space, (0, 0))
    # palnet
    screen.blit(planet, (400 - width / 2, 300 - height / 2))
    # ship
    angle = wrap_angle(angle + 0.1)  # 转动
    pos.x = math.cos(math.radians(angle)) * radius
    pos.y = math.sin(math.radians(angle)) * radius

    r_angle = -angle + 180
    r_ship = pygame.transform.rotate(ship, r_angle)
    screen.blit(r_ship, (430 + pos.x - width // 2, 370 + pos.y - height // 2))

    # screen.blit(ship,(50,50))
    #print_text(font, 0, 20, "rotation:" + "{:.2f}".format(angle))
    #print_text(font, 400, 20, "rotation angle:" + "{:.2f}".format(r_angle))
    #print_text(font, 400, 20, '你就是我的B612星球',color=(255, 255, 255))
    pygame.display.update()
