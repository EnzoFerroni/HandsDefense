import pygame
from pygame.locals import *
from pygame.transform import scale
import random
import sys
print("ARQEXECU")
pygame.init()

#Enzo Ferroni - 10417100 - 10417100@mackenzista.com.br

#Leonardo Rodrigues - 10418105 - 10418105@mackenzista.com.br

#Mateo Zanette - 10417980 - 10417980@mackenzista.com.br

#Pedro Andrade - 10408394 - 10408394@mackeznista.com.br

#Rafael Neves - 10418316 - 10418316@mackenzista.com.br



screen_width = 1200
screen_height = 720
white = WHITE = (255, 255, 255)
black = BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
tela = "START SCREEN"
red = RED = (255, 0, 0)
yellow = YELLOW = (201, 196, 32)
screen = pygame.display.set_mode((screen_width, screen_height))

class Pausa():

    def __init__(self):
        self.a = True
        self.font_pause = pygame.font.SysFont('comicsans', 38)
        self.font_itens = pygame.font.SysFont('comicsans', 26)
        self.pause_items = ["Continuar", "Libras" , "Sair"]
        self.selected_index = 0
        self.tela = "PAUSA"

        self.image = pygame.image.load('./Imagens/libras/ManualLibrasFundoCinza.png')
        self.image = pygame.transform.scale(self.image,(800,600))
    def resetar(self):
        self.tela = "PAUSA"
        self.selected_index = 0
        

    def font(self,font,size):
        return pygame.font.SysFont(font, size)

    def draw_text(self,text, font, text_col, surface, x, y):
        img = font.render(text, True, text_col)
        imgrect = img.get_rect()
        imgrect.topleft = (x, y)
        surface.blit(img, imgrect)
    def libra(self):
        while True:
            screen.blit(self.image,(screen_width//5,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
            pygame.display.flip()
            
    def pause(self):
        

        #Imagem de fundo quando jogo está pausado
        screen.fill((0,0,0))
        self.draw_text('Pause',self.font_pause,white, screen, screen_width//2 - 40, 250)

        #Mexer pelo menu
        for i, item in enumerate(self.pause_items):
            self.color = white if i == self.selected_index else GRAY
            self.draw_text(item, self.font_itens, self.color, screen, (screen_width//4 + 20) + i * 250, 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.selected_index = (self.selected_index - 1) % len(self.pause_items)
                elif event.key == pygame.K_RIGHT:
                    self.selected_index = (self.selected_index + 1) % len(self.pause_items)
                elif event.key == pygame.K_RETURN:
                    if self.selected_index == 0:
                        self.tela = "JOGO"
                    if self.selected_index == 1:
                        screen.fill((255, 255, 255))
                        self.libra()
                    elif self.selected_index == 2:
                        reset(player, dificuldade_global)
                        self.tela = "MENU"
                            
                            #pygame.quit()
                            #sys.exit()
         


def reset(player, dificuldade_global):
    #Vida do jogador voltado ao máximo e sprite carregado,
    #para reinicar o jogo
    #player = Mago()
    player.life = 3
    player.alive = True
    player.animacaoExec = "IDLE"
    enemy_sprite_group.empty()
    player.score = 0
    #general_sprite_group.add(player)
    player.animacaoSpeed = 0.85
    try:
        general_sprite_group.remove(boss)
    except:
        pass



class MENU():
    def __init__(self):
        self.menu_items = ["Iniciar Jogo", "Selecionar Dificuldade: ", "Sair"]
        self.difficulties = ["Fácil", "Normal", "Difícil"]
        self.selected_index = 0
        self.difficulty_index = 0
        self.selected_difficulty = self.difficulties[self.difficulty_index]

        self.estadoMenu = "START SCREEN"

        self.gameover_items = ["Reiniciar","Tela de inicio"]
        self.vitoria_items = ["Continuar para próxima dificuldade","Tela de inicio"]
        #Texto de vitoria na dificuldade dificil
        self.vitoria_max_difficulty_items = ["Reiniciar", "Tela de inicio"]
        


        self.BLINK_EVENT = pygame.USEREVENT + 0
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(self.BLINK_EVENT, 500)  # Define o intervalo de piscar para 500ms
        self.blink = True  # Controle do piscar

        
        self.font_start = pygame.font.Font('./Fontes/eldermagic.ttf', 38)
        self.font_menu = pygame.font.Font('./Fontes/eldermagic.ttf', 26)

        # Carregar imagens
        self.capa_image = pygame.image.load('./Imagens/Background/capa3.jpg').convert()
        self.background_menu = pygame.image.load('./Imagens/Background/backgroundMenu.jpg').convert()

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
            self.draw_text("Press Enter", self.font_start, WHITE, screen, 475, 550)
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
        self.draw_text("Menu", self.font_start, WHITE, screen, 550, 50)
            
            # Desenha os itens do menu com destaque no item selecionado
        for i, item in enumerate(self.menu_items):
            if i == 1:  # Se for a opção de dificuldade, mostrar a dificuldade selecionada
                item = f"{item}<{self.selected_difficulty}>"
            color = WHITE if i == self.selected_index else GRAY
            self.draw_text(item, self.font_menu, color, screen, 400, 150 + i * 50)

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
    def gameover(self):
            #screen.fill((0,0,0))
            fundoLose = pygame.image.load('./Imagens/Derrota.jpeg').convert()
            fundoLose = pygame.transform.scale(fundoLose, (screen_width, screen_height))
            screen.blit(fundoLose, (0, 0))
            self.draw_text("GAME OVER", self.font_start, RED, screen, 450, 50)

            for i, item in enumerate(self.gameover_items):
                color = WHITE if i == self.selected_index else GRAY
                self.draw_text(item, self.font_menu, color, screen, 350, 150 + i * 50)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.menu_items)
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.menu_items)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_index == 0:
                            reset(player, dificuldade_global)
                            self.estadoMenu = "JOGO"
                        elif self.selected_index == 1:
                            reset(player, dificuldade_global)
                            self.estadoMenu = "MENU"
    #Função de vitória
    def vitoria(self):
        #screen.fill((0,0,0))
        fundoWin = pygame.image.load('./Imagens/Vitoria.jpg').convert()
        fundoWin = pygame.transform.scale(fundoWin, (screen_width, screen_height))
        screen.blit(fundoWin, (0, 0))
        self.draw_text("VITÓRIA", self.font_start, YELLOW, screen, 520, 100)
        #Dificuldade fácil e normal
        if self.difficulty_index < 2:
            for i, item in enumerate(self.vitoria_items):
                color = WHITE if i == self.selected_index else GRAY
                self.draw_text(item, self.font_menu, color, screen, 350, 250 + i * 50)
        #Dificuldade dificil
        else:
            for i, item in enumerate(self.vitoria_max_difficulty_items):
                color = WHITE if i == self.selected_index else GRAY
                self.draw_text(item, self.font_menu, color, screen, 350, 150 + i * 50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.menu_items)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.menu_items)
                elif event.key == pygame.K_RETURN:
                    if self.selected_index == 0:
                        if self.difficulty_index < 2:
                            self.difficulty_index +=1
                            self.selected_difficulty = self.dificuldade_global = self.difficulties[self.difficulty_index]
                            #player.reset()
                            self.estadoMenu = "JOGO"
                        else:
                            #player.reset()
                            self.estadoMenu = "JOGO"
                    elif self.selected_index == 1:
                        reset(player, dificuldade_global)
                        self.estadoMenu = "MENU"
    




class Palavras():
    def __init__(self):
        super(Palavras, self).__init__()
        if dificuldade_global == "Difícil":
            self.lista_palavras = {
                                    "escola": "escola",
                                    "amigo": "amigo",
                                    "familia": "familia",
                                    "trabalho": "trabalho",
                                    "pessoa": "pessoa",
                                    "jardim": "jardim",
                                    "estrada": "estrada",
                                    "animal": "animal",
                                    "sombra": "sombra",
                                    "mundo": "mundo",
                                    "casa": "casa",
                                    "gato": "gato",
                                    "livro": "livro",
                                    "mesa": "mesa",
                                    "dado": "dado",
                                    "rato": "rato",
                                    "pato": "pato",
                                    "fogo": "fogo",
                                    "rio": "rio",
                                    "lua": "lua",
                                    "horas": "horas",
                                    "kiwi": "kiwi",
                                    "xadrez": "xadrez",
                                    "queijo": "queijo",
                                    "yoga": "yoga"
                                }
        elif dificuldade_global == "Normal":
            self.lista_palavras = {
                                    "escola": "escola",
                                    "amigo": "amigo",
                                    "familia": "familia",
                                    "trabalho": "trabalho",
                                    "pessoa": "pessoa",
                                    "jardim": "jardim",
                                    "estrada": "estrada",
                                    "animal": "animal",
                                    "sombra": "sombra",
                                    "mundo": "mundo",
                                    "xadrez": "xadrez",
                                    "queijo": "queijo"
                                }
        elif dificuldade_global == "Fácil":
            self.lista_palavras = {
                                    "casa": "casa",
                                    "gato": "gato",
                                    "livro": "livro",
                                    "mesa": "mesa",
                                    "dado": "dado",
                                    "rato": "rato",
                                    "pato": "pato",
                                    "fogo": "fogo",
                                    "rio": "rio",
                                    "lua": "lua",
                                    "kiwi": "kiwi",
                                    "yoga": "yoga"
                                }
        else:
            self.lista_palavras = {"comece": "comece"}
        #self.palavra = random.choice(list(self.lista_palavras.items()))
        self.convertor()

    def convertor(self):
        tempdic = {}
        letras = "abcdefghijklmnopqrstuvwxyz"
        for chave in self.lista_palavras:
            print(self.lista_palavras)
            print(chave)
            tword = ""
            for letter in chave:
                index = letras.index(letter) + 1
                tword += str(index) + "," 
            tempdic.update({chave: tword})
        self.lista_palavras = tempdic
        self.palavra = random.choice(list(self.lista_palavras.items()))
        print(self.palavra)
        
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super(Boss, self).__init__()
        self.image = pygame.image.load('./Imagens/AgisBoss/Agis1.png')
        self.image = pygame.transform.scale(self.image, (448, 480))
        self.rect = self.image.get_rect()
        self.iniPos = (900, 350)
        self.distInd = 100
        self.position = pygame.math.Vector2(self.iniPos[0], self.iniPos[1])
        self.alive = True
        self.animacaoIndex = 1
        self.animacaoExec = "IDLE"
        self.animacaoSpeed = 0.85
        self.speed = random.randint(1, 3)
        self.mid = True
        self.left = False
        self.right = False
        self.bottom = False
        self.top = False

    def update(self):
        if self.position.x >= self.iniPos[0] + self.distInd:
            self.right = True
            self.left = False
            self.mid = False
        elif self.position.x <= self.iniPos[0] - self.distInd:
            self.right = False
            self.left = True
            self.mid = False
        if self.position.y >= self.iniPos[1] + self.distInd:
            self.bottom = True
            self.top = False
            self.mid = False
        elif self.position.y <= self.iniPos[1] - self.distInd:
            self.bottom = False
            self.top = True
            self.mid = False

        if self.mid:
            self.position.x += self.speed
            self.position.y -= self.speed

        if self.left:
            self.position.x += self.speed
        elif self.right:
            self.position.x -= self.speed
        if self.bottom:
            self.position.y -= self.speed
        elif self.top:
            self.position.y += self.speed

        if self.animacaoIndex <= 15:
            self.image = pygame.image.load('./Imagens/AgisBoss/Agis' + str(int(self.animacaoIndex)) + '.png')
            self.image = pygame.transform.scale(self.image, (448, 480))
            self.animacaoIndex += self.animacaoSpeed
        else:
            self.animacaoIndex = 1

        self.rect.center = self.position


        
        
class Mago(pygame.sprite.Sprite):
    def __init__(self):
        super(Mago, self).__init__()
        self.image = pygame.image.load('./Imagens/Sprite Mago/Wizard Pack/WizardIdle/Idle1.png')
        self.image = pygame.transform.scale(self.image, (233,233))
        #self.image.fill((255, 255, 255))
        self.position = pygame.math.Vector2(100, 615)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.life = 3
        self.alive = True
        self.animacaoIndex = 1
        self.animacaoExec = "IDLE"
        self.animacaoSpeed = 0.85
        self.score = 0
    def update(self):
        self.rect.center = self.position
        if self.alive != True:
            #general_sprite_group.remove(player)
            menu.estadoMenu = "GAMEOVER"
            self.animacaoExec = "DEATH"
        if self.animacaoExec == "IDLE":
            if self.animacaoIndex <= 6:
                self.image = pygame.image.load('./Imagens/Sprite Mago/Wizard Pack/WizardIdle/Idle'+ str(int(self.animacaoIndex)) + '.png')
                self.image = pygame.transform.scale(self.image, (233,233))
                self.animacaoIndex += self.animacaoSpeed
            else:
                self.animacaoIndex = 1
        elif self.animacaoExec == "HIT":
            if self.animacaoIndex <= 4:
                self.image = pygame.image.load('./Imagens/Sprite Mago/Wizard Pack/WizardHit/Hit'+ str(int(self.animacaoIndex)) + '.png')
                self.image = pygame.transform.scale(self.image, (233,233))
                self.animacaoIndex += self.animacaoSpeed
            else:
                self.animacaoExec = "IDLE"
        elif self.animacaoExec == "ATTACK":
            if self.animacaoIndex <= 8:
                self.image = pygame.image.load('./Imagens/Sprite Mago/Wizard Pack/WizardAttack/Attack'+ str(int(self.animacaoIndex)) + '.png')
                self.image = pygame.transform.scale(self.image, (233,233))
                self.animacaoIndex += self.animacaoSpeed
            else:
                self.animacaoExec = "IDLE"
        elif self.animacaoExec == "DEATH":
            self.animacaoSpeed = 0.025
            if self.animacaoIndex <= 7:
                self.image = pygame.image.load('./Imagens/Sprite Mago/Wizard Pack/WizardDeath/Death'+ str(int(self.animacaoIndex)) + '.png')
                self.image = pygame.transform.scale(self.image, (233,233))
                self.animacaoIndex += self.animacaoSpeed
            else:
                self.animacaoExec = "NONE"


    def getHit(self):
        self.animacaoExec = "HIT"
        self.animacaoIndex = 1
            

        print("JOGADOR ATINGIDO")
        self.life -= 1

        if self.life <= 0:
            self.alive = False
        
def draw_lives(screen, life):
        heart_image = pygame.image.load('./Imagens/vida.png')  # Carregue a imagem do coração
        heart_image = pygame.transform.scale(heart_image, (50, 50))  # Redimensiona o coração
        for i in range(life):
            screen.blit(heart_image, (10 + i * 55, 10))  # Posiciona os corações no canto superior esquerdo    

def draw_score(screen, score):
    font = pygame.font.Font("./Fontes/eldermagic.ttf", 30)
    text = font.render(f"Pontuação: {score}", True, WHITE)
    screen.blit(text, (screen_width - 400, 10))  

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        self.alive = True
        self.speed = 5
        #self.image = pygame.Surface((50, 30))
        #self.image.fill((255, 255, 255))
        self.path = "./Imagens/Sprite Esqueleto/EsqueletoAndando/esqueleto"
        if dificuldade_global == "Normal":
            self.path = "./Imagens/Vampire Pack/VampireRun/vamprrun"
        elif dificuldade_global == "Difícil":
            escolha = random.randint(1, 2)
            if escolha == 1:
                self.path = "./Imagens/Vampire Pack/VampireRun/vamprrun"
            if escolha == 2:
                self.path = "./Imagens/Sprite Esqueleto/EsqueletoAndando/esqueleto"
        self.image = pygame.image.load("./Imagens/Sprite Esqueleto/EsqueletoAndando/esqueleto1.png")
        self.image = pygame.transform.scale(self.image, (141, 231))
        self.position = pygame.math.Vector2(1000, 600)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.palavra = Palavras()
        self.hit = False
        self.sinal_image = []
        self.XX = self.position.x - 10
        self.animacaoIndex = 1
        self.animacaoSpeed = 0.85

        listaTemp = self.palavra.palavra[1].split(",")
        listaTemp.pop()
        fat = 0
        for e in listaTemp:
            self.sinal_image.append([pygame.image.load("./Imagens/libras/LibrasSemFundoSemLetra/" + e + ".png"), [self.position.x + fat, self.position.y - 50]])
            fat += 51
        
    def update(self):
        #Movimentação Continua do Inimigo
        self.position.x -= self.speed
        self.rect.center = self.position
        self.updatePos()
        #Verificação dos Limites
        if self.position.x <= 100:
            print("Dano ao Jogador!")
            self.hit = True
            self.alive = False
                
        if self.alive != True:
            print("Inimigo Morto")

        if self.animacaoIndex <= 6:
                self.image = pygame.image.load(self.path + str(int(self.animacaoIndex)) + '.png')
                self.image = pygame.transform.scale(self.image, (141, 231))
                self.animacaoIndex += self.animacaoSpeed
        else:
            self.animacaoIndex = 1

    def updatePos(self):
        for e in self.sinal_image:
            e[1] = [e[1][0] - self.speed, self.position.y - 50]

    def draw_text(self):
        #Renderização do Texto Acima do Inimigo
        self.font = pygame.font.Font("./Fontes/eldermagic.ttf", 50)
        self.text = self.font.render(self.palavra.palavra[0], True, white)
        self.textrect = self.text.get_rect()
        self.textrect.center = (self.position.x, self.position.y - 50)
        screen.blit(self.text, self.textrect)
        self.draw_sinais()

    def draw_sinais(self):
        for i in self.sinal_image:
            pygame.transform.scale(i[0], (5, 5))
            tempRect = i[0].get_rect()
            tempRect.center = (i[1][0], i[1][1])
            screen.blit(pygame.transform.scale(i[0], (50, 50)), tempRect)
        
            
        

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
        self.font = pygame.font.Font("./Fontes/eldermagic.ttf", 25)
        self.text = self.font.render(self.palavra, True, white)
        self.textrect = self.text.get_rect()
        self.textrect.center = (100, 575)
        screen.blit(self.text, self.textrect)



menu = MENU()
dificuldade_global = "NULO"

pausa = Pausa()

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
spawnEspera = random.randint(7000, 7001)
inimigo_frente = None
boss = Boss()




fundo = pygame.image.load('./Imagens/Background/Fácil.png')
fundo = pygame.transform.scale(fundo, (screen_width, screen_height))


pontos_objetivo = 500








     
         
while running:
    clock.tick(60)
    if dificuldade_global == "Fácil":
        pontos_objetivo = 100#500
        spawnEspera = random.randint(7000, 7001)
    elif dificuldade_global == "Normal":
        pontos_objetivo = 200#1000
        spawnEspera = random.randint(7000, 7001)
    elif dificuldade_global == "Difícil":
        pontos_objetivo = 300#1500
        spawnEspera = random.randint(7000, 7001)

    if tela == "JOGO":
        dificuldade_global = menu.selected_difficulty
        if player.score >= pontos_objetivo:
            if dificuldade_global == "Fácil":
                menu.selected_difficulty = dificuldade_global = "Normal"
                pontos_objetivo = 1000
                spawnEspera = random.randint(6000, 6001)
                menu.estadoMenu = "VITORIA"
            elif dificuldade_global == "Normal":
                menu.selected_difficulty = dificuldade_global = "Difícil"
                pontos_objetivo = 1500
                spawnEspera = random.randint(5000, 5001)
                menu.estadoMenu = "VITORIA"
            elif dificuldade_global == "Difícil":
                menu.estadoMenu = "VITORIA"
        if dificuldade_global == "Difícil":
            general_sprite_group.add(boss)

            
            
            



            
        fundo = pygame.image.load('./Imagens/Background/' + dificuldade_global + '.png')
        fundo = pygame.transform.scale(fundo, (screen_width, screen_height))
        screen.blit(fundo, (0, 0))
        draw_lives(screen, player.life)
        pygame.draw.rect(screen, (43, 43, 43), pygame.Rect(790, 7, 300, 40))
        draw_score(screen, player.score)
        #screen.fill((216, 113, 18))
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
                    if event.key == pygame.K_SPACE:
                        print("PAUSA")
                        pausa.resetar()
                        menu.estadoMenu = "PAUSA"
                    try:
                        getPalavra.coletarLetras(event.unicode)
                    except:
                        getPalavra.reset()
                    if getPalavra.verificarPalavra():
                        try:
                            player.animacaoExec = "ATTACK"
                            player.animacaoIndex = 1
                            print("Inimigo Morto")
                            player.score += 50
                            inimigo_frente.alive = False
                            getPalavra.reset()
                        except:
                            print("EXCEPTION")


        for enemy in enemy_sprite_group:
            if enemy.alive == True:
                #enemy.draw_text()
                enemy.draw_sinais()
            else:
                if enemy.hit:
                    player.getHit()
                enemy_sprite_group.remove(enemy)
                getPalavra.reset()


            
        enemy_sprite_group.update()
        enemy_sprite_group.draw(screen)
        general_sprite_group.update()
        general_sprite_group.draw(screen)
        tela = menu.estadoMenu
    elif tela == "PAUSA":
        pausa.pause()
        tela = menu.estadoMenu = pausa.tela 
    elif tela == "START SCREEN":
        tela = menu.estadoMenu
        menu.show_start_screen()
    elif tela == "MENU":
        tela = menu.estadoMenu
        menu.menu()
    elif tela == "GAMEOVER":
        tela = menu.estadoMenu
        menu.gameover()
        try:
            general_sprite_group.remove(boss)
        except:
            pass
        general_sprite_group.update()
        general_sprite_group.draw(screen)
    elif tela == "VITORIA":
        tela = menu.estadoMenu
        menu.vitoria()

        
        

         
        

    pygame.display.flip()

    
pygame.quit()
