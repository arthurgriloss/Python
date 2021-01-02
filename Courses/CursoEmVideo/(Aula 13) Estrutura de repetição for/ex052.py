c = 0
n = int(input('Digite um número inteiro: '))
'''if n == 1 or n == 2:
    print('O número {} é primo'.format(n))
for i in range(2, n):
    if n % i == 0:
        print('O número {} não é primo'.format(n))
        break
    if n == i+1:
        print('O número {} é primo'.format(n))'''
for i in range(1, n+1):
    if n % i == 0:
        c += 1
if c > 2:
    print('O número {} não é primo'.format(n))
else:
    print('O número {} é primo'.format(n))

