'''FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR
O JOGO SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO
QUANTAS VITÓRIAS CONSECUTIVAS ELE TEVE NO FINAL DO JOGO'''
from random import randint

while True:
    num = int(input('Escolha um número de 0 à 10: '))
    pc = randint(1, 10)
    soma = num + pc
    tipo = ' '
    while tipo not in PpIi:
        tipo = str(input('Insira par ou impar: ')).strip().upper()[0]
    par = num % 2 == 0

    if escolha == i and soma == par:
        print('O número {} é {}. Você perdeu!!!'.format(soma, escolha))
        break
    if escolha == p and soma == par:
        cont += 1
    print('Você escolheu {} e digitou o número {}...'.format(p, num))
    print('O computador digitou o número {}...'.format(pc))
    print('Você venceu {} partidas.'.format(cont))
    print(soma)


