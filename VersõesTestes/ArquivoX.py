import pygame
from pygame.locals import *
from pygame.transform import scale
import random

pygame.init()

screen_width = 1200
screen_height = 720
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))


class Palavras():
    def __init__(self):
        super(Palavras, self).__init__()
        self.lista_palavras = {"Libras": "Libras"}
        self.palavra = random.choice(list(self.lista_palavras.items()))
        

        
        
        



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
        #Movimentação Continua do Inimigo
        self.position.x -= self.speed
        self.rect.center = self.position
        #Verificação dos Limites
        if self.position.x < 100:
            print("Dano ao Jogador!")

    def draw_text(self):
        #Renderização do Texto Acima do Inimigo
        self.font = pygame.font.SysFont(None, 50)
        self.text = self.font.render(self.palavra.palavra[0], True, white)
        self.textrect = self.text.get_rect()
        self.textrect.center = (self.position.x, self.position.y - 50)
        screen.blit(self.text, self.textrect)
        



        
         
        





running = True

enemy_sprite_group = pygame.sprite.Group()
eteste = Enemy1()
enemy_sprite_group.add(eteste)


while running:
    screen.fill((234, 189, 130))
    for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    for enemy in enemy_sprite_group:
        if enemy.alive == True:
            enemy.draw_text()
        else:
            enemy_sprite_group.remove(enemy)
        
    enemy_sprite_group.update()

    enemy_sprite_group.draw(screen)


    pygame.display.flip()

    
pygame.quit()
