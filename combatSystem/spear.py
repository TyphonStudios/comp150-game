import pygame
import math

class spear:
    def __init__(self, parent):
        self.image = pygame.image.load('spear.png')
        self.parent = parent
        self.rect = self.image.get_rect()
        self.inAttack = False
        self.attackStart = 0
        self.animationLength = 0.3 * 1000 # Milliseconds
        self.animationDistance = 10

    def draw(self, surface):
        posX = self.parent.x
        posY = self.parent.y

        # Adjust in a direction +90 degrees to the direction pointed at
        posX += math.sin(math.radians(self.parent.angle + 90)) * 80
        posY += math.cos(math.radians(self.parent.angle + 90)) * 80

        # Animation
        if self.inAttack:
            posX -= math.sin(math.radians(self.parent.angle)) * 60
            posY -= math.cos(math.radians(self.parent.angle)) * 60

        if self.inAttack:
            time = pygame.time.get_ticks() - self.attackStart
            if time >= self.animationLength:
                self.inAttack = False

        rotImage = pygame.transform.rotate(self.image, self.parent.angle)
        rotRect = rotImage.get_rect(center=self.parent.rect.center)
        surface.blit(rotImage, (posX + rotRect.x, posY + rotRect.y))

    def attack(self):
        if self.inAttack:
            return
        self.attackStart = pygame.time.get_ticks()
        self.inAttack = True