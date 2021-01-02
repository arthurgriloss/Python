from time import sleep
from random import randint
cont = 1
computador = randint(0, 10)
print('Pensei em um número de 0 a 10', end='')
for i in range(0, 3):
    sleep(1)
    print('.', end='')
jogador = int(input('\nConsegue adivinhar?: '))
while computador != jogador:
    for i in range(0, 3):
        sleep(1)
        print('.', end='')
    cont += 1
    if computador > jogador:
        print('\nMeu número é maior vacilão! ERROU!')
    if computador < jogador:
        print('\nMeu número é menor vacilão! ERROU!')
    jogador = int(input('tente novamente: '))
for i in range(0, 3):
    sleep(1)
    print('.', end='')
print('PARABENS! Você acertou depois de {} tentativas'.format(cont))
