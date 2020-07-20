nome = str(input('Insira o seu nome: '))
if nome == 'ronaldo' or nome == 'bernardo':
    print('Acesso liberado!Seja bem vindo {}!'.format(nome.upper()))
elif nome == 'pedro':
    print('Acesso negado!Tente de novo amanhã.')
elif nome == 'ilma':
    print('Alerta, tentativa de invasão!')
else:
    print('Usuário não cadastrado!Cadastre-se agora.')
