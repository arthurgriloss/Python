option = 'y'
soma = 0
cont = 0
while option == 'y':
    cont += 1
    n = int(input('Digite o {}º número: '.format(cont)))
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    option = input('Deseja continuar a operação ? [y/n] ').strip().lower()
print('''Você digitou {} valores
o maior valor digitado foi {}
o menor valor digitado foi {}
a media dos valores digitados foi {:.1f}'''. format(cont, maior, menor, soma/cont))
