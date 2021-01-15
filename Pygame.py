import pygame
from random import randrange
pygame.init()
x = 355 #limite do carro direita 520 - esquerda 190 - centro 355
y = 450
pos_x = 200
pos_y = -250
pos_x_a = 150
pos_y_a = -450
pos_x_b = 300
pos_y_b = -650
pos_x_c = 150
pos_y_c = -850
pos_x_d = 300
pos_y_d = -1050
pos_x_e = 150
pos_y_e = -1250
timer = 0
tempo_seg = 0

velocidade = 50
velo_outros = 10

pista = pygame.image.load('pista_pygame.png')
carro = pygame.image.load('F1_pygame.png')
policia = pygame.image.load('police_car.png')
ambulancia = pygame.image.load('ambulance_car.png')
black_car = pygame.image.load('black_car.png')
red_car = pygame.image.load('red_car.png')
white_car = pygame.image.load('white_car.png')
yellow_car = pygame.image.load('yellow_car.png')

#Configuração do temporizador
#criado objeto 'font' + Método do pygame para configurar fontes
font = pygame.font.SysFont('arial black', 30)
#Objeto texto em formato retangular
texto = font.render('Tempo: ', True, (255,255,255), (0,0,0))
#Posicionamento do retangulo
pos_texto = texto.get_rect()
#Posicionamento do texto no retangulo
pos_texto.center = (65,50)

# Método utilizado para definir tamanho das figuras(fazer uma para cada)
red_car = pygame.transform.scale(red_car, (90, 140))
black_car = pygame.transform.scale(black_car, (90, 140))
white_car = pygame.transform.scale(white_car, (90, 140))
ambulancia = pygame.transform.scale(ambulancia, (90, 140))

#Método utilizado para definir o tamanho da janela
janela = pygame.display.set_mode((800, 600))


#Método utilizado para nomear o cabeçalho da janela
pygame.display.set_caption('Car Escape')

#Loop utilizado para manter a janela aberta enquanto não clicar no 'X' vermelho para sair
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    #Condicional criada quando for disparado algum evento (exemplo, um clique em sair)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Váriavel criada para os controles do teclado
    comandos = pygame.key.get_pressed()
    #if comandos[pygame.K_UP]:
        #y -= velocidade
    #if comandos[pygame.K_DOWN]:
        #y += velocidade
    if comandos[pygame.K_LEFT] and x >= 206:
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 501:
        x += velocidade

    #Condição que faz o carro sumir e aparecer na tela
    if (pos_y >= 650) and (pos_y_a >= 650) and (pos_y_b >= 650) and (pos_y_c >= 650) and (pos_y_d >= 650) and (pos_y_e >= 650):
        pos_y = randrange(-100, -500, -499)  #policia
        pos_y_a = randrange(-300, -600, -599) #vermelho
        pos_y_b = randrange(-2000, -3000, -2999)  #amarelo
        pos_y_c = randrange(-600, -1300, -1299)  #preto
        pos_y_d = randrange(-1000, -1700, -1699)  #ambulancia
        pos_y_e = randrange(-600, -2000, -1999)  #branco

    #Lógica para controlar o tempo incrementa a cada 1 segundo
    if (timer < 20):
        timer += 1
    else:
        tempo_seg += 1
        texto = font.render('Tempo: '+str(tempo_seg), True, (255,255,255), (0,0,0))
        timer = 0

    #Dimensiona a imagem pista na janela
    janela.blit(pista, (22.5, 0))

    #Posiciona a imagem carro na pista
    janela.blit(carro, (x, y))
    janela.blit(policia, (pos_x, pos_y))
    janela.blit(red_car, (pos_x_a + 200, pos_y_a))
    janela.blit(yellow_car, (pos_x_b + 200, pos_y_b))
    janela.blit(black_car, (pos_x_c + 50, pos_y_c))
    janela.blit(ambulancia, (pos_x_d + 200, pos_y_d))
    janela.blit(white_car, (pos_x_e + 200, pos_y_e))
    janela.blit(texto,pos_texto)


    #Método para criar uma forma de objeto na tela
    #1ºparametro cor em RGB - 2ºparametro posição vetor x,y - 3ºparametro diametro do raio circle
    #pygame.draw.circle(janela, (100,50,0), (x,y), 50)

    #Decrementa a velocidade dos outros carros
    pos_y += velo_outros + 10
    pos_y_a += velo_outros + 10
    pos_y_b += velo_outros + 30
    pos_y_c += velo_outros + 15
    pos_y_d += velo_outros + 30
    pos_y_e += velo_outros + 10

    #Atualiza a tela depois de fazer o circle
    pygame.display.update()

pygame.quit()

