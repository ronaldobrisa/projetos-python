'''FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM
E INFORME DE ACORDO COM A SUA IDADE
SE ELE AINDA VAI SE ALISTAR NO SERVIÇO MILITAR
SE É A HORA DE SE ALISTAR OU SE JÁ PASSOU O TEMPO DE ALISTAMENTO
O PROGRAMA DEVERÁ MOSTRAR TAMBÉM O TEMPO QUE FALTA
OU QUE PASSOU DO PRAZO'''
from datetime import date
nasc = int(input('Insira seu ano de nascimento: '))
mes = date.today().year
idade = mes - nasc
falta = (18 - idade)
passou = (idade - 18)
if idade < 18:
    print('Falta {} ano(s) para você se alistar.'.format(falta))
elif idade == 18:
    print('É hora de se alistar!')
else:
    print('Já passou {} ano(s) do prazo.'.format(passou))

