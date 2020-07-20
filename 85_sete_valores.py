'''minha solução
princ = []
temp = []
par = []
impar = []
while True:
    for n in range(0, 7):
        temp.append(int(input(f'Digite o {n}º valor: ')))
        princ.append(temp[:])

    break
for p, v in enumerate(temp):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('~='*15)
print(f'Os valores pares são: {par}', end='')
print(f'\nOs valores ímpares são: {impar}', end='')
#print(f'{}')'''

'''solução guanabara'''
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Insira o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
        num[0].sort()
    else:
        num[1].append(valor)
        num[1].sort()
print('~='*15)
print(f'Pares {num[0]}', end='')
print(f'\nÍmpares {num[1]}', end='')




