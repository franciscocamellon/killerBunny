import pygame
import sys
from pygame.locals import *

# CONSTANTES
# Constantes para o tamanho da tela
LARGURA_TELA = 640
ALTURA_TELA = 480
# Será utilizado para a velocidade do jogo
FPS = 200
# cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)


def carregaImagens():
    global coelho
    global grama
    global castelo
    coelho = pygame.image.load("src/images/dude.png")
    grama = pygame.image.load("src/images/grass.png")
    castelo = pygame.image.load("src/images/castle.png")


def desenharArena():
    carregaImagens()
    for x in range(LARGURA_TELA//grama.get_width()+1):
        for y in range(ALTURA_TELA//grama.get_height()+1):
            DISPLAYSURF.blit(grama, (x*100, y*100))

    for y in range(30, 350, 105):
        DISPLAYSURF.blit(castelo, (0, y))


def desenhaCoelho(coelhoPos):
    DISPLAYSURF.blit(coelho, (coelhoPos[0], coelhoPos[1]))


def moveCoelho(teclas, coelhoPos):
    if teclas[0] and coelhoPos[1] > 0:
        coelhoPos[1] -= 5
    elif teclas[2] and coelhoPos[1] < 420:
        coelhoPos[1] += 5
    if teclas[1] and coelhoPos[0] > 0:
        coelhoPos[0] -= 5
    elif teclas[3] and coelhoPos[0] < 570:
        coelhoPos[0] += 5
    return coelhoPos

# Função principal


def main():
    pygame.init()
    global DISPLAYSURF

    # indices 0,1,2 e3 sao respectivamente as teclas ‘w’, ‘s’, ‘a’ e ‘d’
    teclas = [False, False, False, False]
    coelhoPos = [100, 100]

    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Mamãe Coelho')
    terminou = False

    while not terminou:  # Loop principal do jogo
        for event in pygame.event.get():
            if event.type == QUIT:
                terminou = True

        # Enquanto estiver pressionado, o coelho vai se mexer
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                teclas[0] = True
            elif event.key == K_a:
                teclas[1] = True
            elif event.key == K_s:
                teclas[2] = True
            elif event.key == K_d:
                teclas[3] = True

        # No momento que parou de pressionar a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                teclas[0] = False
            elif event.key == pygame.K_a:
                teclas[1] = False
            elif event.key == pygame.K_s:
                teclas[2] = False
            elif event.key == pygame.K_d:
                teclas[3] = False

        desenharArena()
        coelhoPos = moveCoelho(teclas, coelhoPos)
        desenhaCoelho(coelhoPos)

        pygame.display.update()

    # Finaliza a janela do jogo
    pygame.display.quit()
    # Finaliza o pygame
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
