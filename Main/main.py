"""
Author: Connor Sean Rodgers, Zakary Bruce-Kyle
Class: Main
"""
#Imports
from __future__ import division
import pygame
import sys
import math
from pygame.locals import *
from spear import *
from classEnemy import *
import classSpawnPoint
import dice

SCORE = 0
"""
========================================================================================================================
Player Class
Define init
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
        self.hp = 100
        self.alive = True


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
Define init
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
    Randomly select a spawn point from a predefined list, these points are along 3 sides of the screen and an enemy can
    spawn on any one of these 12 spawn points with an even chance

Define moveTowardsPlayer
    Checks the distance between the enemy object and the player object, then accordingly adjusts it's X and Y co-ordinates
    in order to
========================================================================================================================
"""
class Enemy(object):
    def __init__(self, tag = 0):
        self.tag = tag
        self.image = pygame.image.load('ball.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.x = 0
        self.y = 0
        self.angle = 0
        self.speed = 2
        self.rect = self.image.get_rect()
        self.statLine = createEnemyStats()
        self.hp = self.statLine[0]
        self.strength = self.statLine[1]
        self.dexterity = self.statLine[2]
        self.perception = self.statLine[3]
        self.constitution = self.statLine[4]
# ----------------------------------------------------------------------------------------------------------------------
    def draw(self, surface):
        rotImage = pygame.transform.rotate(self.image, (1 * self.angle))
        rotRect = rotImage.get_rect(center = self.rect.center)
        self.angle = math.atan2((self.x - objPlayer.x), (self.y -  objPlayer.y))
        surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))
        surface.blit(self.image, (self.x,self.y))
# ----------------------------------------------------------------------------------------------------------------------
    def spawn(self):
        """
        Spawn function
         This function makes use of a random number seed to spawn an enemy in a random unoccupied location.
        """
        mustSpawn = True
        while mustSpawn == True:
            side = dice.rollThree() # calculate if the enemy will spawn along the top, bottom or flank
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                position = dice.rollThree()                if spawnPointsTop[position].boolPointOccupied == False:
                    self.x = spawnPointsTop[position].x
                    self.y = spawnPointsTop[position].y
                    spawnPointsTop[position].boolPointOccupied = True  # set spawn to occupied
                    mustSpawn = False
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            elif side == 2:
                position = dice.rollThree()                if spawnPointsFlank[position].boolPointOccupied == False:
                    self.x = spawnPointsFlank[position].x
                    self.y = spawnPointsFlank[position].y
                    spawnPointsFlank[position].boolPointOccupied = True  # set spawn to occupied
                    mustSpawn = False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            else:
                position = dice.rollThree()
                if spawnPointsBottom[position].boolPointOccupied == False:
                    self.x = spawnPointsBottom[position].x
                    self.y = spawnPointsBottom[position].y
                    spawnPointsBottom[position].boolPointOccupied = True  # set spawn to occupied
                    mustSpawn = False

# ----------------------------------------------------------------------------------------------------------------------
    def moveTowardsPlayer(self):
        enemyDistance = 160
        distance = math.sqrt(((objPlayer.x - self.x)**2) + ((objPlayer.y - self.y)**2))
        if self.tag != 1:
            enemyDistance = math.sqrt(((objEnemy.x - self.x)**2) + ((objEnemy.y - self.y)**2))
        if distance > 150 and enemyDistance > 150:
            if self.x > objPlayer.x:
                self.x -= 1
            elif self.x < objPlayer.x:
                self.x += 1
            else:
                self.x = self.x

            if self.y > objPlayer.y:
                self.y -= 1
            elif self.y < objPlayer.y:
                self.y += 1
            else:
                self.y = self.y
# ----------------------------------------------------------------------------------------------------------------------#=======================================================================================================================
def refresh():
    global SCORE
    if objPlayer.hp <= 0:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 60)
        gameOverText = font.render("GAME OVER", True, ((255,0,0)), ((0,0,0)))
        scoreText = font.render(("Score:" + str(SCORE)), True, ((255, 0, 0)), ((0, 0, 0)))
        screen.blit(gameOverText,(400,450))
        screen.blit(scoreText, (450, 550))
        pygame.display.update()
        objPlayer.alive = False
    for enemy in objWeapon.enemies:
        if enemy.hp <= 0:
            enemy.hp = 100
            enemy.spawn()
            SCORE += 10

    return True
#=======================================================================================================================
pygame.init()
# ----------------------------------------------------------------------------------------------------------------------
screenX, screenY = 1000, 1000
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Gaze Of Balor")
# ----------------------------------------------------------------------------------------------------------------------
objPlayer = Player()
objWeapon = spear(objPlayer)
objEnemy = Enemy(1)
objEnemyii = Enemy(2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
objWeapon.enemies.append(objEnemy)
objWeapon.enemies.append(objEnemyii)
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
spawnTi = classSpawnPoint.spawnPoint(0,0)
spawnTii = classSpawnPoint.spawnPoint(160,0)
spawnTiii = classSpawnPoint.spawnPoint(360,0)
spawnTiv = classSpawnPoint.spawnPoint(760, 0)
spawnFi = classSpawnPoint.spawnPoint(800, 0)
spawnFii = classSpawnPoint.spawnPoint(800, 200)
spawnFiii = classSpawnPoint.spawnPoint(800, 400)
spawnFiv= classSpawnPoint.spawnPoint(800, 540)
spawnBi = classSpawnPoint.spawnPoint(0, 800)
spawnBii = classSpawnPoint.spawnPoint(160, 800)
spawnBiii = classSpawnPoint.spawnPoint(360, 800)
spawnBiv = classSpawnPoint.spawnPoint(760, 800)

# ----------------------------------------------------------------------------------------------------------------------
spawnPointsTop = {
    0: spawnTi,
    1: spawnTii,
    2: spawnTiii,
    3: spawnTiv
}
# ----------------------------------------------------------------------------------------------------------------------
spawnPointsFlank = {
    0: spawnFi,
    1: spawnFii,
    2: spawnFiii,
    3: spawnFiv
}
# ----------------------------------------------------------------------------------------------------------------------
spawnPointsBottom = {
    0: spawnBi,
    1: spawnBii,
    2: spawnBiii,
    3: spawnBiv
}
# ----------------------------------------------------------------------------------------------------------------------
objEnemy.spawn()
objEnemyii.spawn()
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
        # Debug Player HP to 0
        if keys[K_BACKSPACE]:
            objPlayer.hp = 0
    if objPlayer.alive == True:
        screen.fill((255, 255, 255))
        objEnemy.moveTowardsPlayer()
        objEnemyii.moveTowardsPlayer()
        objPlayer.draw(screen)
        objWeapon.draw(screen)
        objEnemy.draw(screen)
        objEnemyii.draw(screen)
        pygame.display.update()
        refresh()
        clock.tick(40)