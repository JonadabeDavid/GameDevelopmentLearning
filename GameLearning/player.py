import random

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/nave.png")
        self.image = pygame.transform.scale(self.image, [300, 60])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speedY = 0
        self.speedX = 0
        self.accelerationY = 0.1
        self.accelerationX = 0.1
    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speedY -= self.accelerationY
        elif keys[pygame.K_s]:
            self.speedY += self.accelerationY
        elif keys[pygame.K_d]:
            self.speedX += self.accelerationX
        elif keys[pygame.K_a]:
            self.speedX -= self.accelerationX
        else:
            self.speedY *= 0.95
            self.speedX *= 0.95

        self.rect.y += self.speedY
        self.rect.x += self.speedX

        if self.rect.top < 0:
            self.rect.top = 0
            self.speedY = 0
        if self.rect.bottom > 720:
            self.rect.bottom = 720
            self.speedY = 0