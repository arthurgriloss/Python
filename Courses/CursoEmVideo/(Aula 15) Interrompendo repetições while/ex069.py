cont = menores = homens = maiores = 0
while True:
    cont += 1
    print(f'----- {cont}ª pessoa -----')
    idade = int(input(f'Qual a idade da {cont}ª pessoa? '))
    while True:
        sexo = input(f'Qual o sexo da {cont}ª pessoa? [m/f] ').strip().upper()
        if sexo in 'MF':
            break
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menores += 1
    if idade > 18:
        maiores += 1
    while True:
        escolha = input('Deseja continuar? digite [y] se sim ou qualquer outra tecla para finalizar o programa: ').strip().upper()
        if escolha in 'YN':
            break
    if escolha == 'N':
        break
print(f'''\nVocê adicionou:
{homens} homens
{menores} mulheres menores de 20 anos
{maiores} pessoas mair de 18
Programa finalizado!''')