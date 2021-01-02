total = mais = menor = nomenor = cont = 0
while True:
    nome = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    if preco > 1000:
        mais += 1
    if cont == 0:
        nomenor = nome
        menor = preco
    else:
        if menor > preco:
            menor = preco
            nomenor = nome
    cont += 1
    while True:
        escolha = input('Deseja adicionar outro produto? [y/n] ').upper().strip()
        if escolha in 'YN':
            break
    print('-' * 20)
    if escolha == 'N':
        break
print(f'''Você comprou {cont} produtos.
O total gasto foi {total:.2f}.
Você comprou {mais} produtos acima de R$1000,00.
O produto mais barato comprado foi {nomenor} que custa R${menor:.2f}.
Programa encerrado!''')
