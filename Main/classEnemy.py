"""
========================================================================================================================
Author: Connor Sean Rodgers
Program: Enemy Class
Purpose: Blueprint for the enemies and the creation of these enemies
========================================================================================================================
"""

import random
import math
import pygame

from random import randint

# ----------------------------------------------------------------------------------------------------------------------
def __init__(self):
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
    """
    Draw function
    This function draws the enemy sprites including any rotations that have happened.
    """
    rotImage = pygame.transform.rotate(self.image, (1 * self.angle))
    rotRect = rotImage.get_rect(center=self.rect.center)
    surface.blit(rotImage, (self.x + rotRect.x, self.y + rotRect.y))
    surface.blit(self.image, (self.x, self.y))
    pygame.display.update
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
enemyHP = 0
enemyStrength = 0
enemyDexterity = 0
enemyPerception = 0
enemyConstitution = 0
diceFour = 0
diceSix = 0
diceTen = 0
diceHundred = 0
diceTwelve = 0
diceTwenty = 0
enemyStats = [enemyHP,enemyStrength,enemyDexterity,enemyPerception,enemyConstitution]
# ----------------------------------------------------------------------------------------------------------------------
def createEnemyStats():
    enemyCreationPoints = 36
    enemyHP = 0
    enemyStrength = 0
    enemyDexterity = 0
    enemyPerception = 0
    enemyConstitution = 0
    while (enemyCreationPoints > 0):
        diceFour = randint(1,4)
        if diceFour == 1:
            enemyStrength += 1
        elif diceFour == 2:
            enemyDexterity += 1
        elif diceFour == 3:
            enemyPerception += 1
        else:
            enemyConstitution += 1
        enemyCreationPoints -= 1
    print "Strength:" + str(enemyStrength)
    print "Dexterity:" + str(enemyDexterity)
    print "Perception:" + str(enemyPerception)
    print "Constitution:" + str(enemyConstitution)
    enemyHP = enemyConstitution * 10
    print "HP:" + str(enemyHP)
    enemyStats = [enemyHP, enemyStrength, enemyDexterity, enemyPerception, enemyConstitution]
    return enemyStats
# ----------------------------------------------------------------------------------------------------------------------
def spawnEnemies(enemyStats):
    enemyStats = createEnemyStats()
    self.HP = enemyStats[0]
    self.Strength = enemyStats[1]
    self.Dexterity = enemyStats[2]
    self.Perception = enemyStats[3]
    self.Constitution = enemyStats[4]
    return 0
# ----------------------------------------------------------------------------------------------------------------------


# spawn
#   - no overlap
#   - off screen
#   - x spawn points of screen
#       - if spawn point 1 contins enemy{
#           - Generate list without spawn point 1
#           - Spawn enemy in random spawn point}
# moving
#   - move towards player
#   - cone of influence for steering behaviour
#       - look at direction that the collision is moving and make use of the vectors to rotate to avoid colision while
#           remaining on the same path
#           - line interception?
#               - polygon testing?
# attacking/defending
#   -D&D
# death
"""
for x in range (1...4){
    "spawnPointT" + x
}

"""
