def mensagem(nome, hora):
    if hora < 12:
        print (f'Bom dia {nome}!')
    elif hora < 18:
        print(f'Boa tarde {nome}!')
    else:
        print (f'Boa noite {nome}!')
    return

hora=(int(input('Digite a hora:')))
nome=(str(input('Digite seu nome:')))
mensagem(nome,hora)