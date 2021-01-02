def diminuir(price, fraction):
    res = price - price * fraction / 100
    return res


def aumentar(price, fraction):
    res = price + price * fraction / 100
    return res


def dobro(price):
    return price*2


def metade(price):
    return price/2
