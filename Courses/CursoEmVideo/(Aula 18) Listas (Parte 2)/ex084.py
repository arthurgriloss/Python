lista = list()
maior = menor = 0
while True:
    dado = [input('Nome: '), float(input('Peso: '))]
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if maior < dado[1]:
            maior = dado[1]
        if menor > dado[1]:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    op = input('Deseja encerrar o programa? [y/n] ').upper().strip()
    if op == 'Y':
        break
print(f'Ao todo, você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi {maior} de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {menor} de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
