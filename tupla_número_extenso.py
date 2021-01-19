extenso = ('zero', 'hum', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    digito = int(input('Digite um número de 0 a 20: '))
    if 0 <= digito <= 20:
        break
    print('Tente novamente! ', end='')
print(f'O número digitado foi: {extenso[digito]}')