'''A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA
QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA
DE ACORDO COM A IDADE
ATÉ 9 ANOS MIRIM
ATÉ 14 ANOS INFANTIL
ATÉ 19 ANOS JUNIOR
ATÉ 20 ANOS SENIOR
ACIMA DE 20 ANOS MASTER'''
from datetime import date
ano = int(input('Insira o ano de nascimento do atleta: '))
n = date.today().year
i = n - ano
if i <= 9:
    print('Categoria mirim')
elif i > 9 and i <= 14:
    print('Categoria infantil')
elif i > 14 and i <= 19:
    print('Categoria junior')
elif i == 20:
    print('Categoria senior')
else:
    print('Categoria master')

