termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
quant = int(input('Digite quantos termos você deseja visualizar: '))
while quant > 0:
    print(termo, end=' ')
    termo += razao
    quant -= 1
