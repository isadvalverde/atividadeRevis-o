def login(usuario, senha):
    if usuario == 'adm'and senha == '123':
        print('Login realizado com sucesso')
    else:
        print('Usuário ou senha incorretos')
    return

usuario=(input('Digite seu usuário: '))
senha= (input('Digite sua senha: '))
login(usuario,senha)

