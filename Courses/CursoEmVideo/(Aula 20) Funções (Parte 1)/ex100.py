from random import randint
numeros = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
        print(n, end=' ')
    print('Pronto!')


def somaPar():
    soma = 0
    for e in numeros:
        if e % 2 == 0:
            soma += e
    print(f'Somando os valores pares de {numeros}, temos {soma}')


# main program
sorteia()
somaPar()
