'''ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER
PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
1 PARA BINÁRIO 2 PARA OCTAL OU 3 PARA HEXADECIMAL'''

num = int(input('Insira um número: '))
base = int(input('Escolha o número correspondente a base de conversão\n '
                 '1 BINÁRIO - 2 OCTAL - 3 HEXADECIMAL: '))
b = num.bin()
h = num.hex()
o = num.oct()
res = num
if num / 2 % 0 and num / 2 % 1:
    print(b)
elif num / 16:
    print(h)
else: num / 8
print(o)
