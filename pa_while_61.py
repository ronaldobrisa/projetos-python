'''REFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO
DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO
A ESTRUTURA WHILE'''
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
while termo <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1




