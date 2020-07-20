'''ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO n INTEIRO QUALQUER
E MOSTRE NA TELA OS n PRIMEIROS ELEMENTOS DE UMA
SEQUÊNCIA DE FIBONACCI
ex: 0 1 1 2 3 5 8'''
termos = int(input('Quantos termos você quer mostrar? '))
primeiro = 0 #A sequência de fibonacci sempre começa por 0(zero)
segundo = 1 #O segundo termo sempre é 1
cont = 3 #Se eu tenho o primeiro e o segundo termo,
         # começo a contar a partir do terceiro
while cont <= termos:
    terceiro = primeiro + segundo
    print(terceiro, end=' , ')
    #Para que se dê a sequência
    primeiro = segundo #O primeiro torna-se segundo
    segundo = terceiro #O segundo torna-se terceiro
    cont += 1
print('fim')
