times = ('Flamengo', 'Corinthians', 'Vasco', 'Chapecoense', 'Fluminense', 'Botafogo', 'Gremio', 'Santos',
         'Bahia', 'Palmeiras')
print('Os cinco primeiros colocados são:\n', times[:5])
print('Os quatro ultimos colocados são:\n', times[-4:])
print('Os times em ordem alphabetica:\n', sorted(times))
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
