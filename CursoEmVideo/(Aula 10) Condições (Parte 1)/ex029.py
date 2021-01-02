speed = int(input('Escreva a velocidade do carro em km/h: '))
if speed > 80:
    multa = (speed - 80)*7
    print('Você ultrapassou o limite de velocidade \nSua multa é de R${:.2f}'.format(multa))
else:
    print('Parabens! Você é um motorista responsável!')
