import pygame,os,time
os.system("cls")
pygame.init()

tamanho = (800,600) #tupla
tela = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
pygame.display.set_caption("ex1")
branco = (15,120,215)
preto = (0,0,0)
movxbolinha = (400)
direita = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()  
    tela.fill(branco)
    pygame.display.update()
'''    pygame.draw.circle(tela,preto,(movxbolinha,300),50) #bolinha
    pygame.draw.line(tela,preto,(100,100),(300,100), 1) #linha
    pygame.draw.rect(tela,preto,(400,100,200,50),1) #rect x,y,largura,altura
    
    pygame.display.update()
    if direita == True:
        if movxbolinha <800:
            movxbolinha = movxbolinha+10
        else:
            direita = False
    else:
        if movxbolinha > 0:
            movxbolinha = movxbolinha -10
        else:
            direita = True
    #clock.tick(120)'''



pygame.quit