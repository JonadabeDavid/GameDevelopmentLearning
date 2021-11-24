import random
import pygame

class Shoot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/bullet.png")
        self.image = pygame.transform.scale(self.image, [80, 30])
        self.rect = self.image.get_rect()

        self.speed = 4

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 1280:
            self.kill()