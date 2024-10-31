import pygame
from pygame.locals import *
from pygame.transform import scale
import random

pygame.init()

screen_width = 1200
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))

pause_text= pygame.font.SysFont("comicsans", 115).render("Pause", True, pygame.color.Color("White"))
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.alive = True
        self.speed = 0.1
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 255, 255))
        self.position = pygame.math.Vector2(1000, 700)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        
    def update(self):
        self.position.x -= self.speed
        self.rect.center = self.position



running, pause = 0,1
state = running

sprite_group = pygame.sprite.Group()
eteste = Enemy()
sprite_group.add(eteste)

while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    state = pause
                if event.key == pygame.K_c:
                    state = running
    else:
        
        screen.fill((0, 0, 0))
        
        if state==running:
            sprite_group.update()
            
            sprite_group.draw(screen)

        elif state==pause:
            screen.blit(pause_text,((screen_width//3),(screen_height//3)))

        pygame.display.flip()
        continue
    break
pygame.quit()
