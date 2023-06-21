number_1 = int(input('n1?'))
number_2 = int(input('n2?'))
number_3 = int(input('n3?'))
lista = [number_1, number_2, number_3]
lista.sort(key=int)
maior = lista[-1]
menor = lista[0]
if lista.count(maior) == 1:
    print(f'Maior: {maior}')
elif lista.count(maior) > 1:
    print(f'Maiores: {maior}')
if lista.count(menor) == 1:
    print(f'Menor: {menor}')
elif lista.count(menor) > 1:
    print(f'Menores: {menor}')
if lista[1] == maior or lista[1] == menor:
    print(f'Não há intermediários nessa lista')
else:
    print(f'O número intermediário é o {lista[1]}')
