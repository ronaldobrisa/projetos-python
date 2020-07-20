'''FAÇA UM PROGRAMA QUE LEIA UMA FRASE E DIGA SE ELA É UM PALÍNDROMO
DESCONSIDERANDO OS ESPAÇOS'''
frase = str(input('\033[34mDigite sua frase: ')).strip().upper()
palavras = frase.split()#separo a frase em palavras
junto = ''.join(palavras)#retiro os espaços das palavras juntando elas
inverso = '' #sem FOR fica inverso = junto[::-1]
#No FOR eu pego a variavel 'JUNTO' que é o resultado do tratamento
# de string e com LEN eu defino o tamanho da string começando
# pela primeira letra(-1) indo até a última(-1)
# e de trás pra frente(-1)
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(junto, inverso)
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')



