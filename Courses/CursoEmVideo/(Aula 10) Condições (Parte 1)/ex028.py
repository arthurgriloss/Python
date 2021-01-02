from random import randint
random = randint(0, 5)
valor = int(input('Tente adivinhar o número inteiro entre 0 e 5 que o computador sorteou:'))
#if type(valor) != type(random):
#    print('Eu disse um número inteiro!')
#else:
print('O computador sorteou {}'.format(random))
print('Você acertou!' if random == valor else 'Você perdeu!')
