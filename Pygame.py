import pygame
from random import randrange
pygame.init()
x = 355 #limite do carro direita 520 - esquerda 190 - centro 355
y = 450
pos_x = 200 #policia
pos_y = -1250
pos_x_a = 355 #vermelho
pos_y_a = -1000
pos_x_b = 500 #amarelo
pos_y_b = -2000
pos_x_c = 200 #preto
pos_y_c = -250
pos_x_d = 500 #ambulancia
pos_y_d = -1000
pos_x_e = 355 #branco
pos_y_e = -5000
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

    # Detecta a colisão do lado esquerdo                   x = 355 y = 450
    if ((x - 100 < pos_x and y - 150 < pos_y)):   #policia pos_x = 200  pos_y = -250
        y = -1200
    if ((x - 100 < pos_x_c and y - 150 < pos_y_c)):  #preto pos_x_c = 200  pos_y_c = -250
        y = -1200
    # Detecta a colisão do lado direito
    if ((x + 50 > pos_x_b and y - 140 < pos_y_b)):      #amarelo pos_x_b = 150 pos_y_b = -450
        y = -1200
    if ((x + 50 > pos_x_d and y - 140 < pos_y_d)):      #ambulancia pos_x_d = 150 pos_y_d = -450
        y = -1200
    # Detecta a colisão do centro
    if ((x + 100 > pos_x_a and y - 150 < pos_y_a)) and ((x - 100 < pos_x_a and y - 140 < pos_y_a)):
        y = -1200
    if ((x + 100 > pos_x_e and y - 150 < pos_y_e)) and ((x - 100 < pos_x_e and y - 140 < pos_y_e)):
        y = -1200
                                           #pos_x_a = 355


    #Condição que faz o carro sumir e aparecer na tela
    if (pos_y >= 650):
        pos_y = randrange(-100, -200, -199)  #policia
    if (pos_y_a >= 650):
        pos_y_a = randrange(-100, -200, -199) #vermelho
    if (pos_y_b >= 650):
        pos_y_b = randrange(-100, -200, -199)  #amarelo
    if (pos_y_c >= 650):
        pos_y_c = randrange(-100, -200, -199)  #preto
    if (pos_y_d >= 650):
        pos_y_d = randrange(-100, -200, -199)  #ambulancia
    if (pos_y_e >= 650):
        pos_y_e = randrange(-100, -200, -199)  #branco

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
    janela.blit(red_car, (pos_x_a, pos_y_a))
    janela.blit(yellow_car, (pos_x_b, pos_y_b))
    janela.blit(black_car, (pos_x_c, pos_y_c))
    janela.blit(ambulancia, (pos_x_d, pos_y_d))
    janela.blit(white_car, (pos_x_e, pos_y_e))
    janela.blit(texto,pos_texto)


    #Método para criar uma forma de objeto na tela
    #1ºparametro cor em RGB - 2ºparametro posição vetor x,y - 3ºparametro diametro do raio circle
    #pygame.draw.circle(janela, (100,50,0), (x,y), 50)

    #Decrementa a velocidade dos outros carros
    pos_y += velo_outros + 5 #policia
    pos_y_a += velo_outros + 15 #red_car
    pos_y_b += velo_outros + 5 #yellow_car
    pos_y_c += velo_outros + 5 #black_car
    pos_y_d += velo_outros + 5 #ambulancia
    pos_y_e += velo_outros + 15 #white_car

    #Atualiza a tela depois de fazer o circle
    pygame.display.update()

pygame.quit()

