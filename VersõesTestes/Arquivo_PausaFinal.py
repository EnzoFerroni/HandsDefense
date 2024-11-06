import pygame
import sys
from pygame.locals import *
from pygame.transform import scale
import random

pygame.init()

pygame.key.set_repeat()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

font_pause = pygame.font.SysFont('comicsans', 38)
font_itens = pygame.font.SysFont('comicsans', 26)

image = pygame.image.load('ManualLibras.png')
image = pygame.transform.scale(image,(800,600))

def font(font,size):
    return pygame.font.SysFont(font, size)

def draw_text(text, font, text_col, surface, x, y):
    img = font.render(text, True, text_col)
    imgrect = img.get_rect()
    imgrect.topleft = (x, y)
    surface.blit(img, imgrect)
    
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.alive = True
        self.speed = 0.1
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 255, 255))
        self.position = pygame.math.Vector2(800, 600)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        
    def update(self):
        self.position.x -= self.speed
        self.rect.center = self.position

def libra():
    while True:
        screen.blit(image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        pygame.display.flip()
                

def pause():
    pause_items = ["Continuar", "Libras" , "Sair"]
    selected_index = 0

    while True:
        #Imagem de fundo quando jogo está pausado
        screen.fill((0,0,0))
        draw_text('Pause',font_pause,'white', screen, 350, 250)

        #Mexer pelo menu
        for i, item in enumerate(pause_items):
            color = "White" if i == selected_index else "Gray"
            draw_text(item, font_itens, color, screen, 100 + i * 250, 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(pause_items)
                elif event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(pause_items)
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:
                        return
                    elif selected_index == 1:
                        libra()
                    elif selected_index == 2:
                        pygame.quit()
                        sys.exit()
                    
        pygame.display.flip()

#Saber se o jogo está rodando ou pausado
running, paused = 0,1
state = running

sprite_group = pygame.sprite.Group()
eteste = Enemy()
sprite_group.add(eteste)

while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                break
            #Muda estado para pausado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    state = paused
    else:
        
        screen.fill((0, 0, 0))
        
        if state==running:
            sprite_group.update()
            
            sprite_group.draw(screen)

        elif state==paused:
            #Menu de pausa
            pause()
            state = running
        pygame.display.flip()
        continue
    break
pygame.quit()
