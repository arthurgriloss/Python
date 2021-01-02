'''numero = input('digite um numero de 0 a 9999:')
print('a unidade é ', numero[3])
print('a desena é ', numero[2])
print('a centena é ', numero[1])
print('o milhar é ', numero[0])'''

numero = int(input('digite um numero de '))
print('a unidade é ', numero % 10)
print('a desena é ', numero //10 % 10)
print('a centena é ', numero //100 % 10)
print('o milhar é ', numero //1000 % 10)
