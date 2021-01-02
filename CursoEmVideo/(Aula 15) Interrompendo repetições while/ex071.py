sedula = cont = 0
saque = float(input('Digite quanto deseja sacar: R$'))
while True:
    if cont == 0:
        valor = 50
    elif cont == 1:
        valor = 20
    elif cont == 2:
        valor = 10
    elif cont == 3:
        valor = 1
    else:
        break
    sedula = saque // valor
    saque -= valor * sedula
    print(f'Total de {sedula:.0f} sedulas de R${valor:.2f}')
    cont += 1
print('Volte sempre!')