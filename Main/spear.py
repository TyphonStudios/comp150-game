"""
Author: Zakary Bruce-Kyle
Class: Spear
"""
import pygame
import math
from random import randint
# ======================================================================================================================
"""
========================================================================================================================
Spear Class
Define init
    sprite = spear
    parent = player
    enemies = array of enemies
    inAttack = whether the attack code is being run or not
    weaponReachProgress = how far the spear is from the player
    weaponReachForwards = whether to move the spear forwards or backwards
    weaponReach = maximum distance the spear can move forwards
    weaponSpeed = how fast the spear attack is

Define draw
    Get the parent's positions (the player) and set that as the origin of the spear,
    then rotate the spear by the parent's angle + 90 degrees and move outwards from the player, by their side.
    If inAttack is true, see if the weapon should move forwards or backwards. Forwards will continue the attack
    whilst backwards will start to bring the spear back to reset inAttack. Then if still going forwards, loop through
    all the enemies to see if they collide with the spear and apply random damage if they do collide then start to
    bring the spear back and make inAttack false. Finally draw the spear with the new coordinates.

Define attack
    Set inAttack to true to start the attack if it's currently false.


========================================================================================================================
"""
class spear():
# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self, parent):
        self.image = pygame.image.load('spear.png')
        self.sizeX = self.image.get_width()
        self.sizeY = self.image.get_height()
        self.parent = parent
        self.rect = self.image.get_rect()
        self.enemies = []

        self.inAttack = False
        self.weaponReachProgress = 0
        self.weaponReachForwards = True
        self.weaponReach = 60
        self.weaponSpeed = 4
# ----------------------------------------------------------------------------------------------------------------------
    def draw(self, surface):
        posX = self.parent.x
        posY = self.parent.y
        # Adjust in a direction +90 degrees to the direction pointed at
        posX += math.sin(math.radians(self.parent.angle + 90)) * 80
        posY += math.cos(math.radians(self.parent.angle + 90)) * 80

        # Check if collided
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if self.inAttack:
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if self.weaponReachForwards: # If weapon going forwards
# ......................................................................................................................
                if self.weaponReachProgress >= self.weaponReach:
                    self.weaponReachForwards = False
# ......................................................................................................................
                else:
                    # Collision check
                    tempX = posX - math.sin(math.radians(self.parent.angle)) * self.weaponReachProgress
                    tempY = posY - math.cos(math.radians(self.parent.angle)) * self.weaponReachProgress

                    # For each pixel that we can move forwards to
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    for i in xrange(self.weaponSpeed):
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        for enemy in xrange(len(self.enemies)):
                            # Debug hitbox
                            #pygame.draw.rect(surface, (255,0,0), (tempX + 40, tempY, self.sizeX, self.sizeY))
                            # Check if our hitbox collides with an enemy
# **********************************************************************************************************************
                            if pygame.Rect(tempX + 40, tempY, self.sizeX, self.sizeY).colliderect(
                                    pygame.Rect(self.enemies[enemy].x, self.enemies[enemy].y,
                                                self.enemies[enemy].sizeX, self.enemies[enemy].sizeY)):
                                # If a collision occurs, move the spear back
                                self.enemies[enemy].hp = self.enemies[enemy].hp - randint(12,27)
                                self.weaponReachForwards = False
                                break
# **********************************************************************************************************************
                            else:
                                # No collisions, carry on moving the spear forwards
                                tempX = posX - math.sin(math.radians(self.parent.angle)) * self.weaponReachProgress
                                tempY = posY - math.cos(math.radians(self.parent.angle)) * self.weaponReachProgress
                                self.weaponReachProgress = min(self.weaponReachProgress + 1, self.weaponReach)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            else:
                # When the spear is all the way back, stop the animation
                if self.weaponReachProgress <= 1:
                    self.inAttack = False
                    self.weaponReachForwards = True
                else:
                    self.weaponReachProgress = max(self.weaponReachProgress - self.weaponSpeed, 0)

            # Move the spear forwards/backwards
            posX -= math.sin(math.radians(self.parent.angle)) * self.weaponReachProgress
            posY -= math.cos(math.radians(self.parent.angle)) * self.weaponReachProgress

        # Draw the spear
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        rotImage = pygame.transform.rotate(self.image, self.parent.angle)
        rotRect = rotImage.get_rect(center=self.parent.rect.center)
        surface.blit(rotImage, (posX + rotRect.x, posY + rotRect.y))
# ----------------------------------------------------------------------------------------------------------------------
    def attack(self):
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if self.inAttack:
            return
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.inAttack = True