matrix = [[], [], []]
for c in range(0, 3):
    for i in range(0, 3):
        matrix[c].append(int(input(f'Digite um valor para [{c}, {i}]: ')))
for c in range(0, 3):
    print('\n')
    for i in range(0, 3):
        print(f'{matrix[c][i]:^5}', end='')
