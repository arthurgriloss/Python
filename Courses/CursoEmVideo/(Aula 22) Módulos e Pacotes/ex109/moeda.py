def moeda(price=0, moeda='R$ '):
    return f'{moeda}{price:.2f}'.replace('.', ',')


def diminuir(price=0, fraction=0, formato=True):
    res = price - price * fraction / 100
    return moeda(res) if formato is True else res


def aumentar(price=0, fraction=0, formato=True):
    res = price + price * fraction / 100
    return moeda(res) if formato is True else res


def dobro(price=0, formato=True):
    return moeda(price*2) if formato is True else price*2


def metade(price=0, formato=True):
    return moeda(price/2) if formato is True else price/2
