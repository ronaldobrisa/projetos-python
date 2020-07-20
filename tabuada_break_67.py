'''FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NÚMEROS UM DE CADA VEZ
PARA CADA VALOR DIGITADO PELO USUÁRIO
O PROGRAMA SERA INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO'''
from time import sleep
cont = 0
tabuada = 1
resposta = 0
while True:
    print('~='*12)
    tabuada = int(input('Digite um número: '))
    print('~='*12)
    if tabuada <= 0:
        print('Número inválido!!!')
        break
    for cont in range(1, 11, 1):
        resposta = tabuada * cont
        cont + 1
        sleep(1)
        print('{} x {} = {}'.format(tabuada, cont, resposta))
print('FIM!!!')


