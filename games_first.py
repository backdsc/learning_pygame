import pygame
from pygame.locals import*
from sys import exit
from random import randint

#inicio
pygame.font.init()
pygame.init()

pygame.mixer.music.set_volume(0.05)
musica_defundo = pygame.mixer_music.load('Jazz at Mladost Club - No More Blues.mp3')
pygame.mixer_music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin (1).wav')

largura = 640
altura = 480

x = largura / 2
y = altura / 2


pontos = 0
font = pygame.font.SysFont('arial', 40, False)

x_azul = randint(40, 600)
y_azul = randint(50, 430)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("dream")

relogio = pygame.time.Clock()


while True:
    relogio.tick(90)
    tela.fill((0,0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = font.render(mensagem, False, (255,155,255))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
            '''
        if event.type==KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20  '''
            
    if pygame.key.get_pressed()[K_a]:
                x = x - 5
    if pygame.key.get_pressed()[K_d]:
                x = x + 5
    if pygame.key.get_pressed()[K_w]:
                y = y - 5
    if pygame.key.get_pressed()[K_s]:
                y = y + 5
    ret_vermelho = pygame.draw.rect(tela, (255, 0,0), (x, y, 60, 60))
    ret_azul = pygame.draw.rect(tela, (0, 180, 240 ), (x_azul, y_azul, 60, 60))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()

    tela.blit(texto_formatado, (450,40))
    pygame.display.update()