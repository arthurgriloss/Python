def factorial(num, show=False):

    """-> Calcula o fatorial de um número"""

    if show:
        fac = 1
        for c in range(num, 0, -1):
            fac *= c
            if c > 1:
                print(f'{c} x', end = ' ')
            else:
                print('1 =', end=' ')
        return fac
    else:
        fac = 1
        for c in range(num, 0, -1):
            fac *= c
        return fac


# programa principal
print(factorial(5, show=True))
help(factorial)