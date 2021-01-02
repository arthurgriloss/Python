numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desessete', 'Dezoito', 'Desenove', 'Vinte')
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        break
print(f'Voce digitou o número {numeros[n]}')
