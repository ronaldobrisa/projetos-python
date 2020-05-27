from random import choice
a = input('Insira o nome do primeiro aluno: ')
b = input('Insira o nome do segundo aluno: ')
c = input('Insira o nome do terceiro aluno: ')
d = input('Insira o nome do quarto aluno: ')
lista = [a,b,c,d]#o colchetes cria uma lista
sorteado = choice(lista)
print('O aluno escolhido foi: {}'.format(sorteado))