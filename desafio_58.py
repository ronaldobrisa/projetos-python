'''MELHORE O JOGO DO DESAFIO 28 ONDE O COMPUTADOR VAI PENSAR
EM UM NÚMERO ENTRE 0 E 10 SÓ QUE AGORA O JOGADOR VAI TENTAR
ADIVINHAR ATÉ ACERTAR MOSTRANDO NO FINAL QUANTOS PALPITES
FORAM NECESSARIOS PARA VENCER'''
from random import choice
pc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha = choice(pc)
palpite = 0
num = 0
while num != escolha:
    palpite += 1
    num = int(input('Escolha um número de 0 à 10: '))
    print('Tente outra vez!')
    print('-'*30)
print('Parabéns, você acertou!'
      ' O total de palpites foi {}'.format(palpite))


