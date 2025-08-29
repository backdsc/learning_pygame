import pygame

#iniicalizar
pygame.init()

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("TesteMan")

tamanho_bola = 15
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0, 750, tamanho_jogador, 20)

qtde_blocos = 8
qtde_linhas = 5
qtde_ttl = qtde_blocos * qtde_linhas

def criar_blocos(qtde_blocos, qtde_linhas):
    blocos = []
    #criar os blocos
    bloco = pygame.Rect(50 , 50, 80, 15)
    blocos.append(bloco)
    bloco = pygame.Rect( 190, 50, 85, 12)
    blocos.append(bloco)
    bloco = pygame.Rect( 320, 50, 85, 12)
    blocos.append(bloco)
    return blocos
cores = {
    "branca": (255, 255, 255),
    "preta": (0,0,0),
    "amarela": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0,255,0)
}

fim_jogo = False
pontuacao = 0
movimento_bola = [1, -1]

#criar as funções do jogo


#desenhar as coisas na tela

def desenhar_inicio_jogo():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["amarela"], jogador)
    pygame.draw.rect(tela, cores["branca"], bola)
    
def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)


desenhar_inicio_jogo()
blocos = criar_blocos(qtde_blocos, qtde_linhas)
desenhar_blocos(blocos)

#criar um loop infinito

while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True



    pygame.time.wait(2)
    pygame.display.flip()

pygame.quit()