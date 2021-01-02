for i in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa em kg: '.format(i+1)))
    if i == 0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {:.2f} kg e o menor peso foi {:.2f} kg'.format(maior, menor))
