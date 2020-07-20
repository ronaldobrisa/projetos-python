m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        m[linha][coluna] = int(input(f'Digite o valor para [{linha},{coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{m[linha][coluna]:^5}]', end='')
        if m[linha][coluna] % 2 == 0:
            spar += m[linha][coluna]
    print()
print(f'A soma dos números pares é: {spar}')
print('*'*20)
for l in range(0, 3):
    scol += m[l][2]
print(f'A soma da terceira coluna é: {scol}')
print('*'*20)
for c in range(0, 3):
    if c == 0:
        mai = m[1][c]
    elif m[1][c] > mai:
        mai = m[1][c]
print(f'O maior número da 2º linha é: {mai}')

