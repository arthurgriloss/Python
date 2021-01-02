from random import randint
cont = 0
while True:
    option = input('Par ou Impar? [P/I] ').strip().upper()
    n = int(input('Digite um valor de 0 a 10: '))
    comp = randint(0, 10)
    print(f'O computador jogou {comp}...')
    if (comp + n) % 2 == 0:
        if option == 'P':
            cont += 1
            print('Você ganhou! Quero revanche!')
            print('-'*20)
        else:
            print('Perdedoooor!')
            break
    if (comp + n) % 2 != 0:
        if option == 'I':
            cont += 1
            print('Você ganhou! Quero revanche!')
            print('-' * 20)
        else:
            print('Perdedoooor!')
            break
print(f'Jogo finalizado. Você ganhou {cont} vezes antes de perder.')
