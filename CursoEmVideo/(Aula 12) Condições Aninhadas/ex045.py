from random import randint
from time import sleep
itens = ['PEDRA', 'PAPEL', 'TESOURA']
pc = randint(0, 2)
vc = int(input('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
if vc > 2:
    print('Escolha 0, 1, ou 2...')
else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!')
    sleep(0.5)
    print('-='*20)
    print('''Computador jogou {}
    Você jogou {}'''.format(itens[pc], itens[vc]))
    print('-='*20)
    if pc == vc:
        print('EMPATE!!')
    elif pc < vc:
        if pc == 0 and vc == 2:
            print('Você perdeu!')
        else:
            print('Você venceu!!')
    else:
        if vc == 0 and pc == 2:
            print('Você venceu!!')
        else:
            print('Você perdeu!!')
