r1 = float(input('Digite o valor do segmento 1 do triangulo: '))
r2 = float(input('Digite o valor do segmento 2 do triangulo: '))
r3 = float(input('Digite o valor do segmento 3 do triangulo: '))
if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('não é possivel formar um triangulo com os segmentos escolhidos')
else:
    print('O triangulo é', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print ('ISOSCELES')
