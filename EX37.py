number = int(input('digite um número'))
funcao = int(input('O que deseja fazer com esse número?   1.Traduzir para binário  2.Traduzir para hexadecimal'
             '  3. Traduzir para o Octal   4. Nada :)'))
if funcao == 1:
    number = bin(number)
    print(f'O número em binário é {number}!')
elif funcao == 2:
    number = hex(number)
    print(f'O número em hexadecimal é {number}')
elif funcao == 3:
    number = oct(number)
    print(f'O número em octal é {number}')
else:
    print('Beleza então, desgraçado!')
