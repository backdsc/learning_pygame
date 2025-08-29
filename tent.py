import pygame
from pygame.locals import*
from sys import exit

#inicialização
pygame.init()

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Game")

#loop

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (200, 32, 102), (120, 102, 25, 12), (65))
    pygame.display.update()