km = float(input('Quantos quilometros o carro percorreu? '))
dia = int(input('Quantos dias o carro foi utilizado? '))
taxakm = (km * 0.15)
diaria = (dia * 60)
total_aluguel=(diaria+taxakm)
print('O valor total do aluguel do veiculo é de: R${:.2f} '.format(total_aluguel))

