dados = []
pessoas = []
perg = 'SsNn'
mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(dados) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    perg = str(input('Deseja continuar [S]sim ou [N]não: ')).upper().strip()[0]
    if perg != 'S' and perg != 'N':
        perg = str(input('Opção errada! Digite [S]sim ou [N]não: ')).upper().strip()[0]
    if 'S' not in perg:
        break

print('='*50)
print(f'Lista geral: \n{dados}')
print('='*25)
print(f'O número de pessoas cadastradas é: {len(dados)}')
print(f'O maior peso é: {mai}', end='')
for p in dados:
    if p[1] == mai:
        print(f' {p[0]}')
print(f'O menor peso é: {men}', end='')
for p in dados:
    if p[1] == men:
        print(f' {p[0]}')
print('FIM!!!')





