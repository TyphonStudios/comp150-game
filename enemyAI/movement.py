#Imports
from __future__ import division
import pygame
import sys
import math
import time
from pygame.locals import *
import classEnemy
import classSpawnPoint

"""
========================================================================================================================
Player Class
Define self
    sprite = ball
    x = 1
    y = 1
    angle = 0 degrees
    create rectangle around the sprite

Define draw
    detect change in mouse position and x 50 as a sensitivity modifier
    rotate a rectangle around the player to face the mouse
    rotate the player to be back in line with the rectangle
    transfer to screen

Define move_up / move_left / move_down / move_right
    moves the player across the screen whilst stopping them from going
    out of bounds and can reduce the speed by half which is used when
    the player is going diagonally to stop the speed boost.

========================================================================================================================
"""

class Player(object):
    def __init__(self):
        self.image = pygame.image.load('player.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.x = 1
        self.y = 1
        self.angle = 0
        self.speed = 2
        self.rect = self.image.get_rect()

    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, (50 * self.angle))
        rotRect = rotImage.get_rect(center = self.rect.center)
        surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))
        pygame.display.update()

    def move_up(self, half):
        self.y = max(self.y - (self.speed / half), 0)

    def move_left(self, half):
        self.x = max(self.x - (self.speed / half), 0)

    def move_down(self, half):
        self.y = min(self.y + (self.speed / half), screenY - self.sizeY)

    def move_right(self, half):
        self.x = min(self.x + (self.speed / half), screenX - self.sizeX)

classEnemy.spawnEnemies()
class Enemy(object):
    def __init__(self):
        self.image = pygame.image.load('ball.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.x = 400
        self.y = 300
        self.angle = 0
        self.speed = 2
        self.rect = self.image.get_rect()

    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, (1 * self.angle))
        rotRect = rotImage.get_rect(center = self.rect.center)
        surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))
        surface.blit(self.image, (self.x,self.y))
        pygame.display.update

pygame.init()
screenX, screenY = 800, 600
screen = pygame.display.set_mode((screenX, screenY))
objPlayer = Player()
objEnemy = Enemy()
objEnemyii = Enemy()
objEnemyii.x = 100
objEnemyii.y = 300
clock = pygame.time.Clock()
pygame.mouse.set_visible(False) # Hide the cursor, TODO: stop cursor from escaping the window
blnRunning = True
while blnRunning:

    spawnTopOne = classSpawnPoint.spawnPoint()
    spawnTopTwo = classSpawnPoint.spawnPoint()
    spawnTopThree = classSpawnPoint.spawnPoint()
    spawnTopFour = classSpawnPoint.spawnPoint()
    spawnFlankOne = classSpawnPoint.spawnPoint()
    spawnFlankTwo = classSpawnPoint.spawnPoint()
    spawnFlankThree = classSpawnPoint.spawnPoint()
    spawnFlankFour = classSpawnPoint.spawnPoint()
    spawnBottomOne = classSpawnPoint.spawnPoint()
    spawnBottomTwo = classSpawnPoint.spawnPoint()
    spawnBottomThree = classSpawnPoint.spawnPoint()
    spawnBottomFour = classSpawnPoint.spawnPoint()


    for event in pygame.event.get():
        """
        ----------------------------------------------------------------------------------------------------------------
            When the mouse moves fetch the position and rotate the player to face it
        ----------------------------------------------------------------------------------------------------------------
        """
        if event.type == MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            objPlayer.angle = math.atan2((objPlayer.x - mouseX), (objPlayer.y - mouseY))
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
    """
    --------------------------------------------------------------------------------------------------------------------
        When the keyboard is pressed (WASD), move the player
    --------------------------------------------------------------------------------------------------------------------
    """
    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()

        # Check for diagonals
        half = 0
        if keys[K_w]:
            half = min(half + 1, 2)
        if keys[K_a]:
            half = min(half + 1, 2)
        if keys[K_s]:
            half = min(half + 1, 2)
        if keys[K_d]:
            half = min(half + 1, 2)

        # Move the player
        if keys[K_w]:
            objPlayer.move_up(half)
            objEnemy.angle = math.atan2((objEnemy.x - objPlayer.x), (objEnemy.y - objPlayer.y))
            objEnemyii.angle = math.atan2((objEnemyii.x - objPlayer.x), (objEnemyii.y - objPlayer.y))
        if keys[K_a]:
            objPlayer.move_left(half)
            objEnemy.angle = math.atan2((objEnemy.x - objPlayer.x), (objEnemy.y - objPlayer.y))
            objEnemyii.angle = math.atan2((objEnemyii.x - objPlayer.x), (objEnemyii.y - objPlayer.y))
        if keys[K_s]:
            objPlayer.move_down(half)
            objEnemy.angle = math.atan2((objEnemy.x - objPlayer.x), (objEnemy.y - objPlayer.y))
            objEnemyii.angle = math.atan2((objEnemyii.x - objPlayer.x), (objEnemyii.y - objPlayer.y))
        if keys[K_d]:
            objPlayer.move_right(half)
            objEnemy.angle = math.atan2((objEnemy.x - objPlayer.x), (objEnemy.y - objPlayer.y))
            objEnemyii.angle = math.atan2((objEnemyii.x - objPlayer.x), (objEnemyii.y - objPlayer.y))
    screen.fill((255, 255, 255))
    objEnemy.draw(screen)
    objEnemyii.draw(screen)
    objPlayer.draw(screen)
    pygame.display.update()
    clock.tick(40)