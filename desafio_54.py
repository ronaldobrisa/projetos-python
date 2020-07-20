'''CRIE UM PROGRAMA QUE LEIA O NOME E ANO DE NASCIMENTO DE 7 PESSOAS
NO FINAL MOSTRE QUANTAS PESSOAS NÃO ATINGIRAM A MAIORIDADE E QUANTAS
 PESSOAS JÁ SÃO MAIORES'''
from datetime import date
ano = date.today().year
cmaior = 0
cmenor = 0
for c in range(1, 3 + 1):
    nome = str(input('Digite seu nome: '))
    nasc = int(input('Em que ano você nasceu?: '))
    if (ano - nasc) < 21:
        cmenor += 1
    elif (ano - nasc) >= 21:
        cmaior += 1
print('\033[32mO total de maiores é {}.'.format(cmaior))
print('\033[31mO total de menores é {}.'.format(cmenor))
