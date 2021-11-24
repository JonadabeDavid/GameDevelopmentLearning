import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
####

import random
import pygame
from player import Player
from asteroid import Asteroid
from shoot import Shoot

#inicializando o Pygame e criando a janela
pygame.init()
display = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Meu Jogo")

#Groups
objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

#Background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/background_04.jpg")
bg.image = pygame.transform.scale(bg.image, [1280, 720])
bg.rect = bg.image.get_rect()

player = Player(objectGroup)

# Music
pygame.mixer.music.load("data/Theme.mp3")
pygame.mixer.music.play(-1)

# Sounds
shoot = pygame.mixer.Sound("data/Shoot.wav")

gameLoop = True
gameOver = False
timer = 0
clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameOver:
                    shoot.play()
                    newShoot = Shoot(objectGroup, shootGroup)
                    newShoot.rect.center = player.rect.center


        #keys = pygame.key.get_pressed()

        '''if keys[pygame.K_a]:
            guy.rect.x -= 1
        elif keys[pygame.K_d]:
            guy.rect.x += 1'''

        #pygame.draw.rect(display, [225, 255, 255, 255], guy)


        #Update Logic:
        if not gameOver:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newAsteroid = Asteroid(objectGroup, asteroidGroup)

            collisions = pygame.sprite.spritecollide(player, asteroidGroup, False, pygame.sprite.collide_mask)

            if collisions:
                print("Game Over!")
                gameOver = True

            hits = pygame.sprite.groupcollide(shootGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

            #Draw:
            objectGroup.draw(display)
            pygame.display.update()
