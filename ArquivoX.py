import pygame
from pygame.locals import *
from pygame.transform import scale
import random
import sys
print("ARQEXECU")
pygame.init()

screen_width = 1200
screen_height = 720
white = WHITE = (255, 255, 255)
black = BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
tela = "START SCREEN"

screen = pygame.display.set_mode((screen_width, screen_height))

class MENU():
    def __init__(self):
        self.menu_items = ["Iniciar Jogo", "Selecionar Dificuldade: ", "Sair"]
        self.difficulties = ["Fácil", "Normal", "Difícil"]
        self.selected_index = 0
        self.difficulty_index = 0
        self.selected_difficulty = self.difficulties[self.difficulty_index]

        self.estadoMenu = "START SCREEN"
        


        self.BLINK_EVENT = pygame.USEREVENT + 0
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(self.BLINK_EVENT, 500)  # Define o intervalo de piscar para 500ms
        self.blink = True  # Controle do piscar

        
        self.font_start = pygame.font.Font('./Fontes/eldermagic.ttf', 38)
        self.font_menu = pygame.font.Font('./Fontes/eldermagic.ttf', 26)

        # Carregar imagens
        self.capa_image = pygame.image.load('./Imagens/capa3.jpg').convert()
        self.background_menu = pygame.image.load('./Imagens/backgroundMenu.jpg').convert()

        # Redimensionar imagens para caber na tela
        self.capa_image = pygame.transform.scale(self.capa_image, (screen_width, screen_height))
        self.background_menu = pygame.transform.scale(self.background_menu, (screen_width, screen_height))

    # Função para desenhar o texto na tela
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    # Função para a tela inicial (capa)
    def show_start_screen(self):
        screen.blit(self.capa_image, (0, 0))
        if self.blink:
            self.draw_text("Press Enter", self.font_start, WHITE, screen, 275, 550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == self.BLINK_EVENT:
                self.blink = not self.blink  # Alterna entre mostrar e esconder o texto
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("lets")
                    self.estadoMenu = "MENU"  # Sai da tela inicial e vai para o menu

            #pygame.display.flip()
            #clock.tick(60)

    # Função principal do menu
    def menu(self):
        screen.blit(self.background_menu, (0, 0))
        self.draw_text("Menu", self.font_start, WHITE, screen, 350, 50)
            
            # Desenha os itens do menu com destaque no item selecionado
        for i, item in enumerate(self.menu_items):
            if i == 1:  # Se for a opção de dificuldade, mostrar a dificuldade selecionada
                item = f"{item}<{self.selected_difficulty}>"
            color = WHITE if i == self.selected_index else GRAY
            self.draw_text(item, self.font_menu, color, screen, 250, 150 + i * 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.menu_items)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.menu_items)
                elif event.key == pygame.K_RIGHT and self.selected_index == 1:
                        # Mudar dificuldade para a direita
                    self.difficulty_index = (self.difficulty_index + 1) % len(self.difficulties)
                    self.selected_difficulty = dificuldade_global = self.difficulties[self.difficulty_index]
                elif event.key == pygame.K_LEFT and self.selected_index == 1:
                        # Mudar dificuldade para a esquerda
                    self.difficulty_index = (self.difficulty_index - 1) % len(self.difficulties)
                    self.selected_difficulty = dificuldade_global = self.difficulties[self.difficulty_index]
                elif event.key == pygame.K_RETURN:
                    if self.selected_index == 0:
                            # Iniciar o jogo
                        print(f"Iniciando jogo na dificuldade {self.selected_difficulty}...")
                        self.estadoMenu = "JOGO"
                        dificuldade_global = self.selected_difficulty
                    elif self.selected_index == 2:
                            # Sair do jogo
                        pygame.quit()
                        sys.exit()
    




class Palavras():
    def __init__(self):
        super(Palavras, self).__init__()
        if dificuldade_global == "Difícil":
            self.lista_palavras = {"difilicissimo": "difilicissimo"}
        elif dificuldade_global == "Normal":
            self.lista_palavras = {"normal": "normal"}
        elif dificuldade_global == "Fácil":
            self.lista_palavras = {"ez": "ez"}
        else:
            self.lista_palavras = {"comece": "comece"}
        self.palavra = random.choice(list(self.lista_palavras.items()))

    def convertor(self):
        tempdic = {}
        letras = "abcdefghijklmnopqrstuvwxyz"
        for chave, value in self.lista_palavras:
            tword = ""
            for letter in chave:
                index = letras.index(letter)
                tword += str(index)
            tempdic.update({tword: value})
        

        
        
class Mago(pygame.sprite.Sprite):
    def __init__(self):
        super(Mago, self).__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 255, 255))
        self.position = pygame.math.Vector2(100, 700)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.life = 3
        self.alive = True
    def update(self):
        self.rect.center = self.position
        if self.alive != True:
            print("JOGADOR PERDEU!!!!!!")

    def getHit(self):
        print("JOGADOR ATINGIDO")
        self.life -= 1
        if self.life <= 0:
            self.alive = False
        
        



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
        self.hit = False
        
        
    def update(self):
        #Movimentação Continua do Inimigo
        self.position.x -= self.speed
        self.rect.center = self.position
        #Verificação dos Limites
        if self.position.x <= 100:
            print("Dano ao Jogador!")
            self.hit = True
            self.alive = False
                
        if self.alive != True:
            print("Inimigo Morto")

    def draw_text(self):
        #Renderização do Texto Acima do Inimigo
        self.font = pygame.font.Font("./Fontes/eldermagic.ttf", 50)
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

    def draw_text(self):
        self.font = pygame.font.Font("./Fontes/eldermagic.ttf", 50)
        self.text = self.font.render(self.palavra, True, white)
        self.textrect = self.text.get_rect()
        self.textrect.center = (100, 650)
        screen.blit(self.text, self.textrect)



menu = MENU()
dificuldade_global = "NULO"



running = True

player = Mago()

general_sprite_group = pygame.sprite.Group()
general_sprite_group.add(player)
enemy_sprite_group = pygame.sprite.Group()
#enemyStart = Enemy1()
#enemy_sprite_group.add(enemyStart)
getPalavra = gerenciadorPalavras()
clock = pygame.time.Clock()
spawnTime = 0
spawnEspera = random.randint(3000, 5000)
inimigo_frente = None


















     
         
while running:
    #clock.tick(60)
    if tela == "JOGO":
        dificuldade_global = menu.selected_difficulty
        screen.fill((234, 189, 130))
        getPalavra.draw_text()
        if len(enemy_sprite_group.sprites()) > 0:
            inimigo_frente = enemy_sprite_group.sprites()[0]
        if inimigo_frente:
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
                if enemy.hit:
                    player.getHit()
                enemy_sprite_group.remove(enemy)
                getPalavra.reset()
            
        enemy_sprite_group.update()
        enemy_sprite_group.draw(screen)
        general_sprite_group.update()
        general_sprite_group.draw(screen)
        
    elif tela == "START SCREEN":
        tela = menu.estadoMenu
        menu.show_start_screen()
    elif tela == "MENU":
        tela = menu.estadoMenu
        menu.menu()

         
        

    pygame.display.flip()

    
pygame.quit()
