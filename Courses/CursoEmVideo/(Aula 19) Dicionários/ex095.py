dic = dict()
gols = list()
lista = list()
while True:
    dic.clear()
    dic['jogador'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {dic["jogador"]} jogou? '))
    gols.clear()
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    dic['gols'] = gols[:]
    dic['total'] = sum(gols)
    lista.append(dic.copy())
    op = input('Deseja continuar [S/N]? ').upper().strip()
    if op == 'N':
        break
print('-='*30)
print(f'{"cod":>3} {"nome":<20} {"gols":<20} {"total":<}')
print('-'*60)
for p, e in enumerate(lista):
        print(f'{p:>3}', end=' ')
        for d in e.values():
            print(f'{str(d):<20}', end=' ')
        print(' ')
while True:
    op = int(input('Quer mostrar os dados de qual jogador? '))
    if 0 > op or op >= len(lista):
        break
    else:
        print(f'----Levantamento do jogador {lista[op]["jogador"]}')
        for p, e in enumerate(lista[op]["gols"]):
            print(f'No jogo {p+1} fez {e} gols')
    print('-'*60)
print('Volte Sempre')
