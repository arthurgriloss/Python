dic = dict()
lista = list()
dic['jogador'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {dic["jogador"]} jogou? '))
for c in range(1, partidas+1):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
    dic['gols'] = lista
    soma = 0
    for e in lista:
        soma += e
    dic['total'] = soma
print('-='*30)
print(dic)
print('-='*30)
for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'''O jogador {dic["jogador"]} jogou {partidas} partidas.''')
for c in range(1, partidas+1):
    print(f'''   => Na partida {c}, fez {dic["gols"][c-1]} gols''')
print(f'Foi um total de {soma} gols')
