n = int(input('Digite um número inteiro: '))
print('[ 1 ] BINÁRIO \n[ 2 ] OCTAL \n[ 3 ] HEXADECIMAL ')
op = input('Escolha uma das bases para conversão: ')
if op == '1':
    print('{} convertido para BINÀRIO é igual a {}'.format(n, bin(n)[2:]))
elif op == '2':
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif op == '3':
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('As opções são somente 1, 2 e 3')
