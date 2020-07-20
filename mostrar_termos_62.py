'''MELHORE O DESAFIO 61, PERGUNTANDO PARA O USUÁRIO SE ELE
QUER MOSTRAR MAIS ALGUNS TERMOS.
O PROGRAMA ENCERRA QUANDO ELE DISSER QUE
QUER MOSTRAR 0 TERMOS'''
primeiro = int(input('insira o primeiro termo: '))
razao = int(input('insira a razão: '))
termo = primeiro
cont = 1
S = 'Ss'
N = 'Nn'
novo = ''
while termo <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
novo = str(input('\nDeseja inserir outro termo? [S]sim ou [N]não? ')).upper()
if novo == 'S':
    primeiro = int(input('insira o primeiro termo: '))
    razao = int(input('insira a razão: '))
if novo == 'N' and primeiro == 0:
    print('Fim do programa!')
if novo == 'S' and primeiro == 0:
    print('Fim do programa!')
