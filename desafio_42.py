'''REFAÇA O DESAFIO 35 DOS TRIANGULOS ACRESCENTANDO O RECURSO
DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO
EQUILÁTERO(TODOS OS LADOS IGUAIS)
ISÓSCELES(DOIS LADOS IGUAIS)
ESCALENO(TODOS OS LADOS DIFERENTES)'''
a = float(input('Insira a medida do lado a: '))
b = float(input('Insira a medida do lado b: '))
c = float(input('Insira a medida do lado c: '))
if a < b + c and b < a + c and c < a + b:
    print('Triângulo Equilátero.')
elif a == b == c:
    print('Triãngulo Isósceles!')
elif a != b and a != c and b != a and b != c and c != a and c != b:
    print('Triângulo Escaleno')
else:
    print('Não é triângulo!')
