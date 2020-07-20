'''la = [[], [], []]
lb = [[], [], []]
lc = [[], [], []]
matriz = []
num = 0
for c in range(1, 11):
    num = int(input(f'Insira o {c}º valor: '))
    la.append(num)
    num.clear()
print('~='*15)
print(matriz)'''

'''solucão guanabara'''
soma = par = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
sep = '=' * 20
titulo = 'MATRIZ'
print(titulo.center(22, '='))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
'''print(matriz[0][0], matriz[0][1], matriz[0][2])
print(matriz[1][0], matriz[1][1], matriz[1][2])
print(matriz[2][0], matriz[2][1], matriz[2][2])'''
