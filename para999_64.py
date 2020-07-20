'''CRIE UM PROGRAMA QUE LEIA VARIOS NÚMEROS INTEIROS PELO TECLADO.
O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999.
QUE É A CONDIÇÃO DE PARADA.
NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS
E QUAL FOI A SOMA ENTRE ELES (desconsiderando o flag).'''
quant = somanum = num = 0
while True:
    num = int(input('Digite um número(999 para parar): '))
    if num == 999:
        break
    quant += 1
    somanum += num
print('A soma dos números é {}, e o total de '
      'números digitados é {}'.format(somanum, quant))
print('FIM')
