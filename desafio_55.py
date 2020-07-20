'''FAÇA UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS. NO FINAL MOSTRE
QUAL FOI O MAIOR E O MENOR PESO LIDOS'''
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Insira o peso da {} pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}kg'.format(maior))
print('O menor peso é {}kg'.format(menor))


