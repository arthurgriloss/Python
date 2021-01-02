n = int(input('Digite o número de termos da sequencia de Fibonacci que deseja visualizar: '))
if n == 1:
    print('0')
else:
    fn1 = 0
    fn2 = 1
    print('{} -> {} '.format(fn1, fn2), end=' ')
    fn3 = 1
while n > 2:
    print('-> {}'.format(fn3), end=' ')
    fn1 = fn2
    fn2 = fn3
    fn3 = fn2 + fn1
    n -= 1
