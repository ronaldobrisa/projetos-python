'''CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS
PELO TECLADO. NO FINAL MOSTRE A MÉDIA ENTRE TODOS OS VALORES
E QUAL FOI O MAIOR E O MENOR VALOR LIDOS, O PROGRAMA DEVE PERGUNTAR
AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES'''
resp = 'Ss'
somanum = 0
media = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Insira um número: '))
    somanum += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
resp = str(input('Quer inserir outro número? ')).upper().strip()[0]
media = somanum / quant
print('A média é: {}'.format(media))
print('O maior valor foi {}.'.format(maior))
print('O menor valor foi {}.'.format(menor))


