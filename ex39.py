ano_atual = 2023
sexo = input('Qual o seu sexo? Digite "M" para masculino e "F" para feminino!')
if sexo == 'M' or sexo == 'm':
    nascimento = int(input('Qual o ano em que você nasceu, camarada?'))
    idade = ano_atual - nascimento
    if idade < 18:
        print(f'Ainda não está na hora de se alistar, volte daqui a {18-idade} anos')
    elif idade == 18:
        print('Ok, já está na hora de se alistar, seja bem vindo ás forças armadas!')
    elif idade > 18:
        print(f'Já se passaram {idade-18} anos desde o seu alistamento obrigatório, você vai preso!')
elif sexo == 'F' or sexo == 'f':
    nascimento = int(input('Qual o ano em que você nasceu, camarada?'))
    idade = ano_atual - nascimento
    if idade < 18:
        print(f'Você é valente, garotinha, mas ainda faltam {18 - idade} anos para que possa se alistar!')
    elif idade == 18:
        print(f'Você fez a escolha certa em servir a pátria, sua contribuição será de grande valia!')
    elif idade > 18:
        print(f'Você passou do período para alistamento em {idade - 18} anos, mas não se preocuper'
              'O seu alistamento não é obrigatório!')
print('Exército Brasileiro! Braço forte, mão amiga!')
