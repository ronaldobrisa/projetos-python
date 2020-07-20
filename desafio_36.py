'''ESCREVA UM PROGRAMA PARA APROVAR O EMPREŚTIMO BANCÁRIO
PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA
O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR
CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA
NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPREŚTIMO SERÁ NEGADO'''
vc = float(input('Qual o valor da casa R$: '))
sal = float(input('Qual o seu salário R$: '))
prazo = float(input('Quantos anos de financiamento: '))
prestacao = vc / (prazo * 12)
limite = (sal / 100) * 30
if prestacao <= limite:
    print('Empréstimo aprovado')
else: print('Empréstimo negado')



