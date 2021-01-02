soma = 0
cont = 0
start = int(input('Digite o primeiro valor do intervalor: '))
end = int(input('Digite o último valor do intervalo: '))
for c in range(start, end, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('\nA soma dos {} valores impares e multiplos de tres no intervalo ({},{}) é {}'.format(cont, start, end, soma))
