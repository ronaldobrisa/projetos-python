'''REFAÇA O EXERCÍCIO 9 MOSTRANDO A TABUADA QUE O USUÁRIO ESCOLHER
SÓ QUE UTILIZANDO O LAÇO FOR'''
tabuada = int(input('Insira um número: '))
print('A tabuada do {} é:'.format(tabuada))
total = 0
for c in range(1, 11):
    if total == total:
        total = tabuada * c
        print('{} x {} = {}'.format(tabuada, c, total))


