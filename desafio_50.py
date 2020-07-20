'''DESENVOLVA UM PROGRAMA QUE LEIA 6 NÚMEROS INTEIROS E MOSTRE
A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR IMPAR
DESCONSIDERE-O'''
cont = 0#variável criada para contar quantos números foram digitados
soma = 0#variável criada para somar os números digitados
#num recebe os números escolhidos
#comando FOR define quantos números serão recebidos
for c in range(1, 7):
    num = int(input('Insira o {} número: '.format(c)))
    if num % 2 == 0:
        soma += num #equivale a soma = soma + num
        cont += 1 #equivale a cont = cont + 1
print('O total de números é {} e a soma é {}.'.format(cont, soma))
