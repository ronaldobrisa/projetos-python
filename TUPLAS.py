#lanche = tupla() lista[] dicionário{}
#TUPLAS EM PYTHON SÃO IMUTÁVEIS
#lanche = ('hamburguer', 'pizza', 'suco', 'pudim')

#Fatiamento de tuplas

#print(f'Eu gosto de, ', lanche[:2])
#print(f'Eu gosto de, ', lanche[-2])
#print(f'Eu gosto de, ', lanche[-2:])

#for comida in lanche:
    #print(f'Eu gosto de {comida}')
#print(f'Comi bastante hj!!!')

#Mostra quantos itens tenho na tupla
#print(len(lanche))

#Contador de posições da tupla usando for e range
#for cont in range(0, len(lanche)):
    #print(cont)

#Contador de posições da tupla mostrando strings usando for e range
#for cont in range(0, len(lanche)):
    #print(f'Eu gosto de',lanche[cont])

#Mostrar a string na tupla e posição
#for cont in range(0, len(lanche)):
    #print(f'Eu gosto de {lanche[cont]}, na posição {cont}')

#Mostrar a string na tupla e posição utilizando o método Enumerate e 2 variáveis
#for pos, comida in enumerate(lanche):
    #print(f'Eu gosto de {comida}, na posição {pos}')

#Utilizando método Sorted para organizar os elementos da tupla alfabeticamente
#print(sorted(lanche))

#Junção de tuplas em ordem crescente
a = (2, 4, 6)
b = (3, 7, 2, 10)
c = a + b
#print(sorted(c))

#Método para contar quantas vezes o respectivo número aparece na tupla
#print(c.count(4))

#Método index mostra em que posição está o respectivo número na tupla
#print(c)
#print(f'posicão {c.index(7)}')

##Método index mostra em que posição está o respectivo número na tupla a partir da posição definida
#print(c)           número | posição
#print(f'posicão {c.index(7, 1)}')

