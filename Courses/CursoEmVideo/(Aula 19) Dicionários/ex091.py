from random import randint
from time import sleep
from operator import itemgetter
lista = list()
dic = dict()
print('Valores sorteados: ')
for c in range(0, 4):
    dic[f'Jogador{c+1}'] = randint(1, 6)
    dic.copy()
for k, v in dic.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
for p, e in enumerate(ranking):
    print(f'O {p+1}º lugar é do {e[0]} com o dado {e[1]}')
    sleep(0.5)
