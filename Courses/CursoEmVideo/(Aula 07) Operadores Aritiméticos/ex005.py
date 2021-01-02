print('Qual é o sucessor e antecessor do numero?')
numero = float(input('Digitite um número:'))
sucessor = numero+1
antecessor = numero-1
print('o sucessor de {} é {:.2f}'.format(numero, sucessor), end=' ')
print('o antecessor de {} é {:.2f}'.format(numero, antecessor))
