'''DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE
UMA PROGRESSÃO ARITMÉTICA. NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS
DESSA PROGRESSÃO'''
a = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão da progressão: '))
an = a + (10 - 1) * r#fórmula para achar o último termo da progressão
for c in range(a, an + r, r):
    print(c, end=' -> ')
print('Acabou!')
