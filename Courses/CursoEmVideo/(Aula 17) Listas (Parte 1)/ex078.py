lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
maior = menor = 0
print(f'Voce digitou os valors{lista}')
for c in range(0, len(lista)):
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'O maior valor foi {maior} na posição', end=' ')
for p, v in enumerate(lista):
    if v == maior:
        print(p+1, end='...')
print(f' E o menor valor foi {menor} na posição', end=' ')
for p, v in enumerate(lista):
    if v == menor:
        print(p+1, end='...')