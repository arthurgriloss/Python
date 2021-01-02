n = soma = cont = 0
while n != 999:
    n = int(input('Digite os numeros que deseja somar (caso deseje encerrar o programa digite 999): '))
    soma += n
    cont += 1
soma -= 999
print('''Você digitou {} números
A soma de todos os números digitados é {}
...
Programa encerrado!'''. format(cont-1, soma))