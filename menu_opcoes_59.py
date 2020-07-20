'''CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE
UM MENU NA TELA [1]SOMAR - [2]MULTIPLICAR - [3]MAIOR -
[4]NOVOS NÚMEROS - [5]SAIR DO PROGRAMA
SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO'''
from time import sleep
opcao = 0
soma = 0
mult = 0
maior = 0
menor = 0
while opcao != 5:
    for v in range(1, 3):
        valor = int(input('Insira o {} valor: '.format(v)))
    print('[1] SOMAR\n[2] MULTIPLCAR\n[3] MAIOR\n[4] NOVOS NÚMEROS'
              '\n[5] SAIR DO PROGRAMA')
    opcao = int(input('Escolha uma opção: '))
    print('=-=' * 30)
    if opcao == 1:
        soma = valor + valor
        print('A soma dos valores é {}'.format(soma))
    elif opcao == 2:
        mult = valor * valor
        print('A multiplicacão dos valores é {}'.format(mult))
    elif opcao == 3:
        maior = valor > valor
        print('O maior valor entre os dois valores é {}'.format(maior))
    elif opcao == 4:
        valor
        print('Por favor, insira novos valores!')
    elif opcao == 5:
        print('Finalizando... Volte sempre!')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 30)
    sleep(2)
print('Fim')





