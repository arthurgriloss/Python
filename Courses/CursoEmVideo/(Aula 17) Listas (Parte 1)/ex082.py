lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    op = input('Deseja sair do programa? [y/n] ').strip().upper()
    if op in 'N':
        break
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    if n % 2 != 0:
        impares.append(n)
print(f'''A lista criada foi {lista}
Os números pares da lista criada são {pares}
Os números impares da lista criada são {impares}''')
