lista = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'''Os valores pares digitados foram {lista[0]}
Os valores impares digitados foram {lista[1]}''')