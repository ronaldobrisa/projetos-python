#teste = list()
#teste.append('ronaldo')
#teste.append(36)
#galera = list()
#galera.append(teste[:])
#teste[0] = 'bernardo'
#teste[1] = '10'
#galera.append(teste[:])
#print(galera)

#galera = [['ronaldo', 19],['benardo', 10],['ilma', 51],['lucas', 28]]
#print(galera[2][0])

#galera = [['ronaldo', 19],['benardo', 10],['ilma', 51],['lucas', 28]]
#for p, g in enumerate(galera):
#    print(f'\nO nome na posição {p} é {g[0]}', end='')

galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Digite nome: ')))
    dados.append(int(input('Digite a idade: ')))
    galera.append(dados[:])
    dados.clear()
print('~='*16)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print('^v'*16)
print(f'Temos {totmai} maiores e {totmen} menores.')


