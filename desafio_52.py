'''FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU
NÃO UM NÚMERO PRIMO'''
#Primeiro passo é inserir um número no INPUT
#Segundo é ler de 1 até o número que eu inseri no laço FOR
#Terceiro é colocar a fórmula ou condições no IF, ELIF, ELSE
#Por último mandar imprimir o resultado final
tot = 0
num = int(input('Insira um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')# \033[33m é o comando de cores
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes!'.format(num, tot))
if tot == 2:
    print('Por isso que {} é primo!'.format(num))
else:
    print('Por isso que {} não é primo!'.format(num))


