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
        self.lista_palavras = {"libras": "libras", "palavras":"palavras", "fortnite":"fortnite", "apple":"apple", "mackenzie":"mackenzie"}
        self.palavra = random.choice(list(self.lista_palavras.items()))
        

        
        
        



class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        self.alive = True
        self.speed = 0.2
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
            self.alive = False
            print("Dano ao Jogador!")
        if self.alive != True:
            print("Inimigo Morto")

    def draw_text(self):
        #Renderização do Texto Acima do Inimigo
        self.font = pygame.font.SysFont(None, 50)
        self.text = self.font.render(self.palavra.palavra[0], True, white)
        self.textrect = self.text.get_rect()
        self.textrect.center = (self.position.x, self.position.y - 50)
        screen.blit(self.text, self.textrect)

    def getText(self):
        return self.palavra.palavra[0]
        

class gerenciadorPalavras():
    def __init__(self):
        self.ativo = True
        self.palavra = ""
        self.palavraAlvo = ""
        self.indice = 0

    def coletarLetras(self, letra):
        print(letra)
        if letra == self.palavraAlvo[self.indice]:
            self.palavra += letra
            if self.indice <= len(self.palavraAlvo) - 1:
                self.indice += 1
        else:
            print("Feitiço Errado!")

    def verificarPalavra(self):
        print("Palavra digitada: " + self.palavra + " e palavra Alvo: " + self.palavraAlvo)
        if self.palavra == self.palavraAlvo:
            return True
    def reset(self):
        self.palavra = ""
        self.palavraAlvo = ""
        self.indice = 0
        
         
        





running = True

enemy_sprite_group = pygame.sprite.Group()
eteste = Enemy1()
enemy_sprite_group.add(eteste)
getPalavra = gerenciadorPalavras()
clock = pygame.time.Clock()
spawnTime = 0
spawnEspera = random.randint(2000, 5000)

while running:
    screen.fill((234, 189, 130))
    if len(enemy_sprite_group.sprites()) > 0:
        inimigo_frente = enemy_sprite_group.sprites()[0]
    getPalavra.palavraAlvo = inimigo_frente.getText()


    if pygame.time.get_ticks() - spawnTime >= spawnEspera:
        spawnTime = pygame.time.get_ticks()
        print("Tempo Passado")
        tempEnemy = Enemy1()
        enemy_sprite_group.add(tempEnemy)

    
    for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                getPalavra.coletarLetras(event.unicode) 
                if getPalavra.verificarPalavra():
                    print("Inimigo Morto")
                    inimigo_frente.alive = False
                    getPalavra.reset()



    for enemy in enemy_sprite_group:
        if enemy.alive == True:
            enemy.draw_text()
        else:
            enemy_sprite_group.remove(enemy)
            getPalavra.reset()
        
    enemy_sprite_group.update()

    enemy_sprite_group.draw(screen)
    #clock.tick(60)

    pygame.display.flip()

    
pygame.quit()
