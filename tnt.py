import pygame
from pygame.locals import*
from sys import exit
from random import randint

#inicialização
pygame.font.init()
pygame.init()


pygame.mixer_music.set_volume(0.8)
musica_de_fundo = pygame.mixer_music.load('Jazz at Mladost Club - No More Blues.mp3')
pygame.mixer_music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480
x = largura / 2
y = altura/ 2
relogio = pygame.time.Clock()
font = pygame.font.SysFont("arial", 40, True, False)
x_azul = randint(40, 60)
y_azul = randint(50, 430)
pontos = 0


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Game")

#loop principal
while True:
    relogio.tick(20)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = font.render(mensagem, True, (255, 255, 255))
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
            if event.type ==K_s:
                y = y + 20
            '''
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20
    ret_verme = pygame.draw.rect(tela, (255, 0, 0),(x, y, 60, 60))
    ret_azul = pygame.draw.rect(tela, (0,120, 250), (x_azul, y_azul, 60, 60 ))

    if ret_verme.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 440)
        pontos = pontos + 1
        barulho_colisao.play()

    tela.blit(texto_formatado, (440, 40))
    pygame.display.update()