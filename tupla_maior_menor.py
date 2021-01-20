from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
#Três formas de imprimir na tela os números sorteados na tupla
print(f'Números sorteados: {n}')

for num in n:
    print(f'{num} ', end='')
'\n'
print(f'\nOs números em ordem crescente são {sorted(n)}')

#Imprime o maior e menor valor sorteado dentro da tupla usando metodo max/min
print(f'O maior valor sorteado foi {max(n)}')
print(f'O maior valor sorteado foi {min(n)}')

