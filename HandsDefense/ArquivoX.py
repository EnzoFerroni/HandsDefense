import pygame
from pygame.locals import *
from pygame.transform import scale
import random

pygame.init()

screen_width = 1200
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))


class Palavras():
    def __init__(self):
        self.lista_palavras = {"Libras": "libras"}
        self.palavra = random.choice(list(self.lista_palavras.items()))
        self.font = pygame.font.Font('freesansbold.ttf', 32)



class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        self.alive = True
        self.speed = 0.1
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 255, 255))
        self.position = pygame.math.Vector2(1000, 700)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.palavra = Palavras()
        
    def update(self):
        self.position.x -= self.speed
        self.rect.center = self.position

         
        





running = True

sprite_group = pygame.sprite.Group()
eteste = Enemy1()
sprite_group.add(eteste)

while running:
    for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    sprite_group.update()

    screen.fill((0, 0, 0))
    sprite_group.draw(screen)


    pygame.display.flip()

    
pygame.quit()
