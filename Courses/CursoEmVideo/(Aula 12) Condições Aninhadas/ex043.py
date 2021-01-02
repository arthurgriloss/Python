peso = float(input('Qual é seu peso em kg? '))
altura = float(input('Qual a sua altura em cm? '))
IMC = peso / (altura / 100)**2
print('Seu IMC é {:.1f}'.format(IMC))
print('Você está', end =' ')
if IMC < 18.5:
    print('ABAIXO DO PESO IDEAL')
elif IMC < 25:
    print('NO PESO IDEAL')
elif IMC < 30:
    print('COM SOBREPESO')
elif IMC < 40:
    print('COM OBESIDADE')
else:
    print('COM OBESIDADE MÓRBIDA')
