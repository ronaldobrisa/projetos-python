'''ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO
CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO
À VISTA(DINHEIRO OU CHEQUE) - 10% DE DESCONTO
À VISTA (NO CARTÃO) - 5% DE DESCONTO
EM ATÉ 2x (NO CARTÃO) - PREÇO NORMAL
3X OU MAIS (NO CARTÃO) - 20% DE JUROS'''
valor = float(input('Digite o valor do produto: '))
formapagto = str(input('Escolha a forma de pagamento:\n'
                       '1 - dinheiro_a_vista\n'  
                       '2 - cheque_a_vista\n'
                       '3 - a vista no cartão\n'
                       '4 - duas vezes no cartão\n'
                       '5 - três vezes no cartão\n'))
dincheque = valor / 100 * 10
vistacartao = valor / 100 * 5
duascartao = valor
trescartao = valor / 100 * 20
if '1' in formapagto:
    print('O valor do produto é: R${:.2f}'.format(valor - dincheque))
elif '2' in formapagto:
    print('O valor do produto é: R${:.2f}'.format(valor - dincheque))
elif '3' in formapagto:
    print('O valor do produto é: R${:.2f}'.format(valor - vistacartao))
elif '4' in formapagto:
    print('O valor do produto é de: R${:.2f}'.format(duascartao))
elif '5' in formapagto:
    print('O valor do produto é de: R${:.2f}'.format(valor + trescartao))
else:
    print('Opção inválida!!!')