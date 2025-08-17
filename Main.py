import pygame
from pygame.locals import *
from sys import exit

#incializando o pygame
pygame.init()
largura = 640
altura = 480
x = largura / 2  # tanto a 'x' quanto a 'y' controla o movimento do persongame
y = altura / 2

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
        if event.type== KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20

    if pygame.key.get_pressed()[K_a]:
        x = x - 2
    if pygame.key.get_pressed()[K_d]:
        x = x + 2
    if pygame.key.get_pressed()[K_s]:
        y = y + 2
    if pygame.key.get_pressed()[K_w]:
        y = y - 2

    ret_ver = pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 62))
    ret_azul = pygame.draw.rect(tela, (0,0,255), (150, 120, 40, 50))

    if ret_ver.colliderect(ret_azul): #Alteração para que ocorra colisão com nome no terminal... aprendendo ainda mais!
        print("comeu")

    pygame.display.update()
