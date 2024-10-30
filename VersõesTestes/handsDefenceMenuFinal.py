import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hands Defence")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonte
font_start = pygame.font.Font('eldermagic.ttf', 38)
font_menu = pygame.font.Font('eldermagic.ttf', 26)

# Carregar imagens
capa_image = pygame.image.load('capa3.jpg').convert()
background_menu = pygame.image.load('backgroundMenu.jpg').convert()

# Redimensionar imagens para caber na tela
capa_image = pygame.transform.scale(capa_image, (screen_width, screen_height))
background_menu = pygame.transform.scale(background_menu, (screen_width, screen_height))

# Função para desenhar o texto na tela
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Função para a tela inicial (capa)
def show_start_screen():
    BLINK_EVENT = pygame.USEREVENT + 0
    clock = pygame.time.Clock()
    pygame.time.set_timer(BLINK_EVENT, 500)  # Define o intervalo de piscar para 500ms
    blink = True  # Controle do piscar
    
    while True:
        screen.blit(capa_image, (0, 0))
        if blink:
            draw_text("Press Enter", font_start, WHITE, screen, 275, 550)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == BLINK_EVENT:
                blink = not blink  # Alterna entre mostrar e esconder o texto
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Sai da tela inicial e vai para o menu

        pygame.display.flip()
        clock.tick(60)

# Função principal do menu
def menu():
    menu_items = ["Iniciar Jogo", "Selecionar Dificuldade: ", "Sair"]
    difficulties = ["Fácil", "Normal", "Difícil"]
    selected_index = 0
    difficulty_index = 0
    selected_difficulty = difficulties[difficulty_index]
    tela == "MENU"
    
    while True:
        screen.blit(background_menu, (0, 0))
        draw_text("Menu", font_start, WHITE, screen, 350, 50)
        
        # Desenha os itens do menu com destaque no item selecionado
        for i, item in enumerate(menu_items):
            if i == 1:  # Se for a opção de dificuldade, mostrar a dificuldade selecionada
                item = f"{item}<{selected_difficulty}>"
            color = WHITE if i == selected_index else GRAY
            draw_text(item, font_menu, color, screen, 250, 150 + i * 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_items)
                elif event.key == pygame.K_RIGHT and selected_index == 1:
                    # Mudar dificuldade para a direita
                    difficulty_index = (difficulty_index + 1) % len(difficulties)
                    selected_difficulty = difficulties[difficulty_index]
                elif event.key == pygame.K_LEFT and selected_index == 1:
                    # Mudar dificuldade para a esquerda
                    difficulty_index = (difficulty_index - 1) % len(difficulties)
                    selected_difficulty = difficulties[difficulty_index]
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:
                        # Iniciar o jogo
                        print(f"Iniciando jogo na dificuldade {selected_difficulty}...")
                        tela = "JOGO"
                        break
                    elif selected_index == 2:
                        # Sair do jogo
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()

# Exibe a tela de início e depois o menu
#show_start_screen()
#menu()
