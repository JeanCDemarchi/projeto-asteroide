import pygame
pygame.init()

tamanho = (800,600)
tela = pygame.display.set_mode(tamanho)
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
'''while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()  
    tela.fill(branco)
    pygame.draw.line(tela,preto,(0,300),(800,300),1)
    pygame.display.update()'''

'''while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()  
    tela.fill(branco)
    pygame.draw.line(tela,preto,(0,0),(800,600),1)
    pygame.display.update()'''

'''while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()  
    tela.fill(branco)
    pygame.draw.line(tela,preto,(50,100),(750,100),1)
    pygame.draw.line(tela,preto,(50,100),(400,550),1)
    pygame.draw.line(tela,preto,(400,550),(750,100),1)
    pygame.display.update()'''

'''while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()  
    tela.fill(branco)
    pygame.draw.line(tela,preto,(0,300),(800,300),1)
    pygame.draw.line(tela,preto,(100,500),(100,100),1)
    pygame.draw.line(tela,preto,(100,100),(200,380),1)
    pygame.draw.line(tela,preto,(200,380),(250,150),1)
    pygame.draw.line(tela,preto,(250,150),(250,450),1)
    pygame.draw.line(tela,preto,(250,450),(500,200),1)
    pygame.draw.line(tela,preto,(500,200),(700,420),1)
    pygame.display.update()'''

'''while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()  
    tela.fill(branco)
    pygame.draw.line(tela,preto,(0,600),(350,350),1)
    pygame.draw.line(tela,preto,(450,250),(800,0),1)
    pygame.draw.circle(tela,vermelho,(400,300),80)
    pygame.display.update()'''

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()  
    tela.fill(branco)
    pygame.draw.line(tela,preto,(60,60),(240,490),3)
    pygame.draw.line(tela,preto,(260,500),(390,310),3)
    pygame.draw.line(tela,preto,(410,300),(590,300),3)
    pygame.draw.circle(tela,vermelho,(50,50),30)
    pygame.draw.circle(tela,vermelho,(250,500),30)
    pygame.draw.circle(tela,vermelho,(400,300),30)
    pygame.draw.circle(tela,vermelho,(600,300),30)
    pygame.display.update()