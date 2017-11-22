#Imports
from __future__ import division
import pygame
import sys
import math
from pygame.locals import *
from spear import *
import random
from random import randint
#from classEnemy import *
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
# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.image = pygame.image.load('player.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.x = 1
        self.y = 1
        self.angle = 0
        self.speed = 2
        self.rect = self.image.get_rect()
# ----------------------------------------------------------------------------------------------------------------------
    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, self.angle)
        rotRect = rotImage.get_rect(center = self.rect.center)
        surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))
# ----------------------------------------------------------------------------------------------------------------------
    def moveUp(self, half):
        self.y = max(self.y - (self.speed / half), 0)
# ----------------------------------------------------------------------------------------------------------------------
    def moveLeft(self, half):
        self.x = max(self.x - (self.speed / half), 0)
# ----------------------------------------------------------------------------------------------------------------------
    def moveDown(self, half):
        self.y = min(self.y + (self.speed / half), screenY - self.sizeY)
# ----------------------------------------------------------------------------------------------------------------------
    def moveRight(self, half):
        self.x = min(self.x + (self.speed / half), screenX - self.sizeX)
# ----------------------------------------------------------------------------------------------------------------------
"""
========================================================================================================================
Enemy Class
Define self
    sprite = ball
    x = 0
    y = 0
    angle = 0 degrees
    create rectangle around the sprite

Define draw
    detect change in mouse position and x 50 as a sensitivity modifier
    rotate a rectangle around the player to face the mouse
    rotate the player to be back in line with the rectangle
    transfer to screen

Define spawn
    Randomly select a spawn point that is predefined, these points are allong 3 sides of the screen and an enemy can
    spawn on any one of these 12 spawn points with an even chance

========================================================================================================================
"""
class Enemy(object):
    def __init__(self):
        self.tag = 0
        self.image = pygame.image.load('ball.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.x = 0
        self.y = 0
        self.angle = 0
        self.speed = 2
        self.rect = self.image.get_rect()
# ----------------------------------------------------------------------------------------------------------------------
    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, (1 * self.angle))
        rotRect = rotImage.get_rect(center = self.rect.center)
        self.angle = math.atan2((self.x - objPlayer.x), (self.y -  objPlayer.y))
        surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))
        surface.blit(self.image, (self.x,self.y))
        pygame.display.update

# ----------------------------------------------------------------------------------------------------------------------
    def spawn(self):
        """
        Spawn function
         This function makes use of a random number seed to spawn an enemy in a random unoccupied location.
        """
        mustSpawn = True
        while mustSpawn == True:
            #print str(spawnPointsTop(0).x)
            side = randint(1,3) # calculate if the enemy will spawn along the top, bottom or flank
            print int(side)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if side == 1:
                                       #  spawn location
                position = randint(0,3)
                print str(spawnPointsTop[position].boolPointOccupied)
                if spawnPointsTop[position].boolPointOccupied == False:
                   # self.spawnPoint = spawnPointsTop[position]
                    self.x = spawnPointsTop[position].x
                    self.y = spawnPointsTop[position].y
                    print str(self.x)
                    print "(" + str(self.x) + "," + str(self.y) + ")"
                    spawnPointsTop[position].boolPointOccupied = True  # set spawn to occupied
                    mustSpawn = False
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            elif side == 2:
                position = randint(0, 3)
                print str(spawnPointsFlank[position].boolPointOccupied)
                if spawnPointsFlank[position].boolPointOccupied == False:
                    #self.spawnPoint = spawnPointsFlank[position]
                    self.x = spawnPointsFlank[position].x
                    self.y = spawnPointsFlank[position].y
                    print "(" + str(self.x) + "," + str(self.y) + ")"
                    spawnPointsFlank[position].boolPointOccupied = True  # set spawn to occupied
                    mustSpawn = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            else:
                position = randint(0, 3)
                print str(spawnPointsBottom[position].boolPointOccupied)
                if spawnPointsBottom[position].boolPointOccupied == False:
                    #self.spawnPoint = spawnPointsBottom[position]
                    self.x = spawnPointsBottom[position].x
                    self.y = spawnPointsBottom[position].y
                    print str(self.x)
                    print "(" + str(self.x) + "," + str(self.y) + ")"
                    spawnPointsBottom[position].boolPointOccupied = True  # set spawn to occupied
                    mustSpawn = False

# ----------------------------------------------------------------------------------------------------------------------
    def moveTowardsPlayer(self):
        enemyDistance = 160
        distance = math.sqrt(((objPlayer.x - self.x)**2)+((objPlayer.y - self.y)**2))
        if self.tag != 1:
            enemyDistance = math.sqrt(((objEnemy.x - self.x)**2)+((objEnemy.y - self.y)**2))
        if distance > 150 and enemyDistance > 150:
            if self.x > objPlayer.x:
                self.x -= 1
            elif self.x < objPlayer.x:
                self.x +=1
            else:
                self.x = self.x

            if self.y > objPlayer.y:
                self.y -= 1
            elif self.y < objPlayer.y:
                self.y +=1
            else:
                self.y = self.y
# ----------------------------------------------------------------------------------------------------------------------
    def enemyAttack(self):
        distance = math.sqrt(((objPlayer.x - self.x) ** 2) + ((objPlayer.y - self.y) ** 2))
        if distance <= 150:
            dammage = self.strength
            print str(dammage)
#=======================================================================================================================
pygame.init()
# ----------------------------------------------------------------------------------------------------------------------
screenX, screenY = 1000, 1000
screen = pygame.display.set_mode((screenX, screenY))
# ----------------------------------------------------------------------------------------------------------------------
objPlayer = Player()
objWeapon = spear(objPlayer)
objEnemy = Enemy()
objEnemyii = Enemy()
#statLine = createEnemyStats()
#objEnemy.spawnEnemies(statLine)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
objWeapon.enemies.append(objEnemy)
# ----------------------------------------------------------------------------------------------------------------------
clock = pygame.time.Clock()
# ----------------------------------------------------------------------------------------------------------------------
hideCursor = True
cursorBindHeld = False
pygame.mouse.set_visible(not hideCursor) # Hide the cursor
pygame.event.set_grab(hideCursor) # Lock the cursor to the window
# ----------------------------------------------------------------------------------------------------------------------
blnRunning = True
spawnPointsTop = []
spawnPointsFlank = []
spawnPointsBottom = []
# ----------------------------------------------------------------------------------------------------------------------
spawnT1 = classSpawnPoint.spawnPoint()
spawnT2 = classSpawnPoint.spawnPoint()
spawnT3 = classSpawnPoint.spawnPoint()
spawnT4 = classSpawnPoint.spawnPoint()
spawnF1 = classSpawnPoint.spawnPoint()
spawnF2 = classSpawnPoint.spawnPoint()
spawnF3 = classSpawnPoint.spawnPoint()
spawnF4 = classSpawnPoint.spawnPoint()
spawnB1 = classSpawnPoint.spawnPoint()
spawnB2 = classSpawnPoint.spawnPoint()
spawnB3 = classSpawnPoint.spawnPoint()
spawnB4 = classSpawnPoint.spawnPoint()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
spawnT1.x = 0
spawnT2.x = 160
spawnT3.x = 360
spawnT4.x = 760
spawnF1.x = 800
spawnF2.x = 800
spawnF3.x = 800
spawnF4.x = 800
spawnB1.x = 0
spawnB2.x = 160
spawnB3.x = 360
spawnB4.x = 760
spawnT1.y = 0
spawnT2.y = 0
spawnT3.y = 0
spawnT4.y = 0
spawnF1.y = 0
spawnF2.y = 200
spawnF3.y = 400
spawnF4.y = 540
spawnB1.y = 600
spawnB2.y = 600
spawnB3.y = 600
spawnB4.y = 600
# ----------------------------------------------------------------------------------------------------------------------
spawnPointsTop = {
    0: spawnT1,
    1: spawnT2,
    2: spawnT3,
    3: spawnT4
}
# ----------------------------------------------------------------------------------------------------------------------
spawnPointsFlank = {
    0: spawnF1,
    1: spawnF2,
    2: spawnF3,
    3: spawnF4
}
# ----------------------------------------------------------------------------------------------------------------------
spawnPointsBottom = {
    0: spawnB1,
    1: spawnB2,
    2: spawnB3,
    3: spawnB4
}
# ----------------------------------------------------------------------------------------------------------------------
objEnemy.spawn()
objEnemy.tag = 1
objEnemyii.spawn()
objEnemyii.tag = 2
# ======================================================================================================================
while blnRunning:

    for event in pygame.event.get():
        """
        ----------------------------------------------------------------------------------------------------------------
            When the mouse moves fetch the position and rotate the player to face it
        ----------------------------------------------------------------------------------------------------------------
        """
        if event.type == MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()

            # Base the mouse position off the centre of the screen
            mouseX -= (screenX / 2)
            mouseY -= (screenY / 2)

            # Workout the angle for the player to face
            angle = math.atan2(mouseY, mouseX) * 180 / math.pi
            objPlayer.angle = 270 - angle

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            objWeapon.attack()

        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Toggle the cursor
            if event.key == pygame.K_ESCAPE:
                if hideCursor:
                    hideCursor = False
                else:
                    hideCursor = True
                pygame.event.set_grab(hideCursor)
                pygame.mouse.set_visible(not hideCursor)

    """
    --------------------------------------------------------------------------------------------------------------------
        When the keyboard is pressed (WASD), move the player
    --------------------------------------------------------------------------------------------------------------------
    """
    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()

        # Check for diagonals
        half = 1
        if keys[K_w] and (keys[K_a] or keys[K_d]):
            half = 2
        if keys[K_s] and (keys[K_a] or keys[K_d]):
            half = 2

        # Move the player
        if keys[K_w]:
            objPlayer.moveUp(half)
        if keys[K_a]:
            objPlayer.moveLeft(half)
        if keys[K_s]:
            objPlayer.moveDown(half)
        if keys[K_d]:
            objPlayer.moveRight(half)

    screen.fill((255, 255, 255))

    objEnemy.moveTowardsPlayer()
    objEnemyii.moveTowardsPlayer()
    #objEnemy.enemyAttack()
    #objEnemyii.enemyAttack()
    objPlayer.draw(screen)
    objWeapon.draw(screen)
    objEnemy.draw(screen)
    objEnemyii.draw(screen)
    pygame.display.update()
    clock.tick(40)