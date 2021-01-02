from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo = - passo
    if passo == 0:
        passo = 1
    if inicio > fim:
        print('-' * 30)
        print(f'Contagem de {inicio} até {fim} de {-passo} em {-passo}')
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
    else:
        print('-' * 30)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
    print('')

# main program

contador(0, 10, 1)
contador(10, 0, 2)
print('-'*30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)