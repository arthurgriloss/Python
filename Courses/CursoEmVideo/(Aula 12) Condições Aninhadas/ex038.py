n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print('{:.2f} é maior'.format(n1))
elif n2 > n1:
    print('{:.2f} é maior'.format(n2))
else:
    print('Os valores são iguais')