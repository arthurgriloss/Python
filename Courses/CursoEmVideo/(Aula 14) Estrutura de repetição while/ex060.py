n = int(input('Digite o número o qual você deseja saber o fatorial: '))
fac = n
i = n
print('{}! = '.format(n), end='')
while i > 1:
    print('{} x '.format(i), end='')
    i -= 1
    fac *= i
print('1 = {}'.format(fac))
