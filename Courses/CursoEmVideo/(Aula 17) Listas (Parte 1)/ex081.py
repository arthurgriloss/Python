lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        op = input('Deseja continuar? [y/n] ').strip().upper()
        if op in 'YN':
            break
    if op == 'N':
        break
lista.sort(reverse=True)
print(f'''Você digitou {len(lista)} elementos
Os valores em ordem decrescente são {lista}''')
if 5 in lista:
    print('O valor 5 foi encontrado na gols!')
else:
    print('O valor 5 não foi encontrado na gols')