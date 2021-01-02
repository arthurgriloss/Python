soma = 0
for i in range(0, 6):
    n = int(input('Digite o número {}: '.format(i+1)))
    if n % 2 == 0:
        soma += n
print('A soma de todos os números pares digitados é:', soma)
