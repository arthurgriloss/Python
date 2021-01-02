lista = [[], [], []]
somap = somac = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para [{i}, {j}]: '))
        lista[i].append(n)
        if i == 1 and j == 0:
            maior = n
        if n > maior:
                maior = n
        if n % 2 == 0:
            somap += n
    somac += lista[i][2]
for i in range(0, 3):
    for j in range(0, 3):
        print(f'{lista[i][j]:^5}', end='')
    print('')
print(f'''
A soma de todos valores pares é {somap}
A soma dos valores da terceira coluna é {somac}
O maior valor da seguda linha é {maior}''')

