from __future__ import division
import pygame
import sys
import math
from pygame.locals import *


class Player(object):
    def __init__(self):
        self.image = pygame.image.load('ball.png')
        self.x = 1
        self.y = 1
        self.angle = 0
        self.rect = self.image.get_rect()

    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, (50*self.angle))
        rotRect = rotImage.get_rect(center = self.rect.center)
        self.x = (rotRect.x)
        self.y = (rotRect.y)
        surface.blit(rotImage, (self.x, self.y))
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((800,600))
objPlayer = Player()
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255,255,255))
    objPlayer.draw(screen)

    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()

            objPlayer.angle = math.atan2((objPlayer.x - mouseX), (objPlayer.y - mouseY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(40)