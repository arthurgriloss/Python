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


def resumo(p=0, taxaa=0, taxab=0):
    print('-'*30)
    print(f'RESUMO DO VALOR:'.center(30))
    print('-' * 30)
    print(f'''Preço analizado: \t{moeda(p)}
Dobro do preço: \t{dobro(p)}
Metade do preço \t{metade(p)}
{taxaa}% de aumento: \t{aumentar(p, taxaa)}
{taxab}% de redução: \t{diminuir(p, taxab)}''')
