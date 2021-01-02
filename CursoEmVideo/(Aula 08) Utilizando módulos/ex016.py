"""
from math import trunc
num = float(input('digite um número decimal:'))
inteiro = trunc(num)
print('o valor inteiro do número {} é {}'. format(num, inteiro))
"""
'''
num = float(input('digite um número decimal:'))
print('o valor inteiro do número {} é {} '.format(num, int(num)))
'''
num = float(input('digite um número em decimal:'))
print('o porção inteira do número {} é {:.0f}'.format(num, num))