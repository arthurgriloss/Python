n = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
quant = int(input('Digite o número de termos que deseja ver: '))
i = quant
rep = 1
c = 0
PA = n
while rep != 0:
    while i > 0:
        print(PA, end=' ')
        i -= 1
        PA += razao
    rep = int(input('\nQuantos termos a mais deseja ver? '))
    c += rep
    i = quant + c
    PA = n
    print('você está visualizando mais {} termos totalizando {} termos'.format(rep, i))

print('Programa encerrado!')

