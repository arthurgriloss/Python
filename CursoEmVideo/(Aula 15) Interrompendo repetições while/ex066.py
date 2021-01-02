cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'''Você digitou {cont} valores.
A soma desses valores é {soma}.
Programa de soma encerrado!''')
