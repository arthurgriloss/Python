lista = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Valor adicionado ao final da gols...')
    else:
        for p, v in enumerate(lista):
            if n <= v:
                lista.insert(p, n)
                print('Valor adicionado na posição', p)
                break
print(lista)
