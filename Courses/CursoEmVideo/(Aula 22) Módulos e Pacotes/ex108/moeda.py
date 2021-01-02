def moeda(price=0, moeda='R$ '):
    return f'{moeda}{price:.2f}'.replace('.', ',')


def diminuir(price=0, fraction=0):
    res = price - price * fraction / 100
    return res


def aumentar(price=0, fraction=0):
    res = price + price * fraction / 100
    return res


def dobro(price=0):
    return price*2


def metade(price=0):
    return price/2
