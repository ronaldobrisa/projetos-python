'''DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA
CALCULE SEU imc E MOSTRE SEU STATUS DE ACORDO COM A TABELA ABAIXO
ABAIXO DE 18,5 - ABAIXO DO PESO
ENTRE 18,5 E 25 - PESO IDEAL
ENTRE 25 E 30 - SOBREPESO
ENTRE 30 E 40 - OBESIDADE
ACIMA DE 40 - OBESIDADE MÓRBIDA'''

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal!')
elif imc >= 25 and imc <= 30:
    print('Cuidado sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('Cuidado obesidade!')
else:
    print('Alerta obesidade!')