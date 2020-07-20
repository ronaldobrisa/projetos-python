'''FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA
MAS SÓ ACEITE OS VALORES m ou f. CASO ESTEJA ERRADO
PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO'''
sexo = ''
M = 'Masculino'
F = 'Feminino'
while sexo != 'MFmf':
    sexo = str(input('Insira o sexo [M] ou [F]: ')).upper()
    if sexo == 'M':
        print('O sexo é {}!'.format(M))
        break
    if sexo == 'F':
        print('O sexo é {}!'.format(F))
        break
print('Fim!')
