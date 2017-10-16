from __future__ import division
import pygame
import sys
import math
from pygame.locals import *


class Cat(object):
    def __init__(self):
        self.image = pygame.image.load('ball.png')
        self.x = 1
        self.y = 1
        self.angle = 0
        self.rect = self.image.get_rect()

    def draw(self, surface):
        mosx = 0
        mosy = 0
        x,y = pygame.mouse.get_pos()
        mosx = (x - self.x)
        mosy = (y - self.y)
        #self.x = 0.9*self.x + mosx
        #self.y = 0.9*self.y + mosy
        rotImage = pygame.transform.rotate(self.image, (50*self.angle))
        rot_rect = rotImage.get_rect(center=self.rect.center)
        self.x = (rot_rect.x)
        self.y = (rot_rect.y)
        surface.blit(rotImage, (self.x, self.y))
        pygame.display.update()
        #print self.angle


pygame.init()
screen = pygame.display.set_mode((800,600))
cat = Cat()
Clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255,255,255))
    cat.draw(screen)

    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()

            cat.angle = math.atan2((cat.x - mouseX), (cat.y - mouseY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    Clock.tick(40)