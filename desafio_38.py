'''ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS
MOSTRANDO NA TELA UMA MENSAGEM: O PRIMEIRO VALOR É MAIOR OU
O SEGUNDO VALOR É MAIOR OU NÃO EXISTE VALOR MAIOR OS DOIS SÃO IGUAIS'''
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')