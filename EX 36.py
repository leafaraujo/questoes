v_casa = int(input('Qual é o valor da casa desejada?'))
salario = float(input('QUal o seu salário?'))
tempo = int(input('Em quantos anos deseja pagar?'))
parcela = salario//tempo
if parcela <= salario * 30 // 100:
    print(f'Empréstimo concedido! Você irá pagar o valor simbólico de R$ {parcela} por mês!')
else:
    print("Empréstimo negado!")