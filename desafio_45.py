'''CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOkenPÔ COM VOCÊ '''
from random import choice
eu = str(input('Escolha um número: 1 PEDRA / 2 PAPEL / 3 TESOURA: \n'))
n = ['1','2','3']
pc = choice(n)
if '1' in eu and pc == '1':
    print('pedra(Eu) x (Pc)pedra = Empate!')
elif '1' in eu and pc == '2':
    print('pedra(Eu) x (Pc)papel = PC ganhou!')
elif '1' in eu and pc == '3':
    print('pedra(Eu) x (Pc)tesoura = EU ganhei!')
elif '2' in eu and pc == '1':
    print('papel(Eu) x (Pc)pedra = EU ganhei!')
elif '2' in eu and pc == '2':
    print('papel(Eu) x (Pc)papel = Empate!')
elif '2' in eu and pc == '3':
    print('papel(Eu) x (Pc)tesoura = PC ganhou!')
elif '3' in eu and pc == '1':
    print('tesoura(Eu) x (Pc)pedra = PC ganhou!')
elif '3' in eu and pc == '2':
    print('tesoura(Eu) x (Pc)papel = EU ganhei!')
elif '3' in eu and pc == '3':
    print('tesoura(Eu) x (Pc)tesoura = Empate!')
else:
    print('Opção inválida!')


