lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Este número ja existe e não será adicionado')
    while True:
        op = input('Deseja continuar? [y/n]').strip().upper()
        if op in 'YN':
            break
    if op == 'N':
        break
lista.sort(reverse=True)
print('Os valores digitados foram ', lista)
