import pygame
from pygame.locals import *
from sys import exit

#incializando o pygame
pygame.init()
largura = 640
altura = 480
x = largura / 2
y = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da velha")
relogio = pygame.time.Clock()

#loop infinito
while True:
    relogio.tick(80)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 62))
    if y >= altura: # fiz algumas alterações aqui, para mover o 'Player'.
        y = 0

    y = y + 1
    pygame.display.update()
