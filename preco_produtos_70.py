'''CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS
O PROGRAMA DEVE PERGUNTAR SE O USUÁRIO QUER CONTINUAR
NO FINAL MOSTRE: QUAL É O TOTAL GASTO NA COMPRA
QUANTOS PRODUTOS CUSTAM MAIS DE R$1000
QUAL É O NOME DO PRODUTO MAIS BARATO'''
N = 'Nn'
S = 'Ss'
resposta = ''
cont = menor = totmil = 0
soma = 0
barato = ''
while True:
    print('+~'*25)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Insira o valor do produto: '))
    cont += 1
    soma += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S]sim ou [N]não? ')).strip().upper()[0]
    if resposta == 'N':
        break
print('='*35)
print('O total gasto na compra foi de: R${:.2f}'.format(soma))
print('A quantidade de produtos que custam mais que R$1000: {}'.format(totmil))
print('O produto mais barato é {} e custa R${:.2f}'.format(barato, menor))
print('Obrigado e volte sempre!')
print('FIM!!!')
