'''CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA
ELETRÔNICO.
NO INÍCIO PERGUNTE QUAL O VALOR A SER SACADO(INTEIRO)
E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÁ
ENTREGUE. CONSIDERE QUE A MÁQUINA CONTÉM CÉDULAS DE:
R$50 , R$20 , R$10 , R$2 E R$1.'''

valor = int(input('Digite o valor a ser sacado R$: '))
total = valor
ced = 50
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print('Total de {} cédulas de R${}'.format(contced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        total = 0
        if total == 0:
            break






