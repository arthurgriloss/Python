def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'\033[0;31mERRO: "{n}" é um preço invalido!\033[m')
        else:
            n = float(n)
            ok = True
        if ok:
            break
    return n
