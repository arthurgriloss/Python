numeros =(int(input('Digite um número: ')),
          int(input('Digite um número: ')),
          int(input('Digite um número: ')),
          int(input('Digite um número: ')))
print(f'Você digitou os números: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}')
cont = 0
for n in numeros:
    if n % 2 == 0:
        print(n, end=', ')
print('foram os números pares digitados')