'''CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS
A CADA PESSOA CADASTRADA O PROGRAMA DEVERÁ PERGUNTAR SE
O USUÁRIO QUER OU NÃO CONTINUAR,
NO FINAL MOSTRE QUANTAS PESSOAS TEM MAIS DE 18 ANOS
QUANTOS HOMENS FORAM CADASTRADOS
QUANTAS MULHERES TEM MENOS DE 20 ANOS'''
M = 'sS'
F = 'fF'
S = 'sS'
N = 'nN'
maior = 0
homem = 0
mulher = 0
resposta = ''
while True:
    idade = int(input('Insira a idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Insira o sexo [M]masculino ou [F]feminino'
                     ': ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resposta = str(input('Quer continuar [S]sim ou [N]não: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('*~'*25)
print('O total de pessoas maiores que 18 anos é: {}'.format(maior))
print('*~'*25)
print('O total de pessoas do sexo masculino são: {}'.format(homem))
print('*~'*25)
print('O total de mulheres menores que 20 anos é: {}'.format(mulher))
print('*~'*25)
print('Obrigado por responder.')


