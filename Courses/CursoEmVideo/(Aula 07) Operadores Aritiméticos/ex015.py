print('valor do aluguel do carro')
dias = int(input('por quantos dias o carro foi alugado?:'))
km = int(input('quantos km foram rodados com o carro?:'))
print('o valor do aluguel é R${:.2f}'.format(60*dias+km*0.15))
