lista = [['No.', 'NOME', 'MÉDIA', 'NOTA1', 'NOTA2']]
cont = 1
while True:
    while True:
        lista.append([cont])
        lista[cont].append(input('Nome: '))
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))
        lista[cont].append((n1 + n2) / 2)
        lista[cont].append(n1)
        lista[cont].append(n2)
        cont += 1
        op = input('Deseja continuar? [y/n] ').upper().strip()
        if op == 'N':
            break
    for i in range(0, len(lista)):
        for j in range(0, 3):
            print(f'{lista[i][j]:<10}', end='')
        print('')
    while True:
        op = int(input('Deseja mostrar a nota de qual aluno?'))
        if 0 < op < len(lista):
            print(f'Notas de {lista[op][1]} são [{lista[op][3]}, {lista[op][4]}]')
        else:
            break
    print('Programa encerrado!')
    break

