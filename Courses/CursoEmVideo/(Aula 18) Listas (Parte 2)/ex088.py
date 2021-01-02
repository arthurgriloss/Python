from random import randint
lista = list()
jogos = int(input('Quantos jogos você deseja gerar?: '))
for c in range(0, jogos):
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
        if len(lista) == 6:
            break
    lista.sort()
    print(f'jogo {c+1}: {lista}')
    lista.clear()