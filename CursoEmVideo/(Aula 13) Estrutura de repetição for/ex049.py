n = int(input('Digite o número o qual deseja saber a tabuada: '))
print('='*20)
for c in range (1, 11):
    print('{} X {} = {}'.format(n, c, n*c))
print('='*20)
