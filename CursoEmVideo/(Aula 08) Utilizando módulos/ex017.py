from math import hypot
catetoO = float(input('digite o valor do cateto oposto:'))
catetoA = float(input('digite o valor do cateto adjacente:'))
print('a hipotenuas dos catetos {} e {} tem o valor de {:.2f}'.format(catetoO, catetoA, hypot(catetoO, catetoA)))
