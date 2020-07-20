'''FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS
NÚMEROS IMPARES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM
NO INTERVALO DE 1 ATÉ 500'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('O total de números impares é {}.'.format(cont))
print('A soma dos impares é {}.'.format(soma))
