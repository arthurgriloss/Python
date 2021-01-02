import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, False)}')
print(f'Aumentando 10% temos {moeda.aumentar(p,10)}')
print(f'Reduzindo 13% temos {moeda.diminuir(p, 13)}')
