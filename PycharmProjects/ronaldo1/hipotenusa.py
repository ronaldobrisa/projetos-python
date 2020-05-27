#import math
#math.exp(2)
#a = float(input('Insira valor do cateto oposto: '))
#b = float(input('Insira o valor do cateto adjascente: '))
#h = math.hypot(a,b)
#print('O valor da hipotenusa é: {:.2}'.format(h))

a = float(input('Insira o valor do cateto oposto: '))
b = float(input('Insira o valor do cateto adjacente: '))
h = (a ** 2 + b ** 2) ** (1/2)
print ('O valor da hipotenusa é: {:.2f}'.format(h))