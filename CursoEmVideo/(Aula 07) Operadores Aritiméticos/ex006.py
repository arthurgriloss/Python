print('qual é o dobro, o triplo, e a raiz quadrada do número?')
numero = float(input('digite um número:'))
print('o dobro de {} é {:>5.3f}\no triplo de {} é {:>5.3f}\na raiz quadrada de {} é {:>5.3f}'.format(numero, numero*2, numero, numero*3, numero, numero**(1/2)))
