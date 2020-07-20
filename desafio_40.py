'''CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO
CALCULE SUA MÉDIA MOSTRANDO SUA MÉDIA NO FINAL DE ACORDO COM
A MÉDIA ATINGIDA
MEDIA ABAIXO DE 5,0 REPROVADO
MEDIA ENTRE 5 E 6,9 RECUPERAÇÃO
MEDIA 7,0 OU SUPERIOR APROVADO'''
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Reprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')
