'''DESENVOLVA UM PROGRAMA QUE LEIA NOME,IDADE E SEXO DE 4 PESSOAS
NO FINAL MOSTRE A MÉDIA DE IDADE DO GRUPO, QUAL É O NOME DO HOMEM
MAIS VELHO E QUANTAS MULHERES TEM MENOS DE 20 ANOS'''
mulhermenor = ''
contmulher = 0
media = 0
somaidade = 0
novo = 0
velho = 0
nomenovo = ''
nomevelho = ''
sexo = 'm', 'f'
for p in range(1, 5):
    print('-'*5,'{} pessoa'.format(p),'-'*5)
    nome = str(input('Insira o seu nome: '))
    idade = int(input('Insira a sua idade: '))
    sexo = str(input('Insira sexo M - Masculino ou F - Feminino: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        novo = idade
        nomenovo = nome
    if sexo in 'Mm' and idade < novo:
        novo = idade
        nomenovo = nome
    if p == 1 and sexo in 'Mm':
            velho = idade
            nomevelho = nome
    if sexo in 'Mm' and idade > velho:
            velho = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulher += 1
        mulhermenor += nome
media = somaidade / 4
print('-'*30)
print('A média de idade é: {:.2f}'.format(media))
print('O homem mais novo é {} com {} anos'.format(nomenovo, novo))
print('O homem mais velho é {} com {} anos'.format(nomevelho, velho))
print('{} são mulheres menores de 20 anos'.format(mulhermenor))
print('Total de {} mulheres'.format(contmulher))