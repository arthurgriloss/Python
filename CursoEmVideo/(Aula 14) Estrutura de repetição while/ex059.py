n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('digite o segundo valor: '))
escolha = 0
while escolha != '5':
    print('-'*10)
    escolha = input('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Qual o maior valor?
[ 4 ] editar os valores
[ 5 ] sair
Que operação deseja efetuar?''')
    print('-'*10)
    if escolha == '1':
        print('\nA soma de {:.2f} e {:.2f} é {:.2f}'.format(n1, n2, n1+n2))
    elif escolha == '2':
        print('\nO produto entre {:.2f} e {:.2f} é {:.2f}'.format(n1, n2, n1 * n2))
    elif escolha == '3':
        print('\nO maior valor é ', n2)
        if n1 > n2:
            print('\nO maior valor é ', n1)
    elif escolha == '4':
        n1 = float(input('\nDigite o novo primeiro valor: '))
        n2 = float(input('digite o novo segundo valor: '))
        print('\nValores alterados para {:.2f} e {:.2f}'.format(n1, n2))
    elif escolha == '5':
        print('Programa encerrado!')
    else:
        print('\nValor invalido, favor escolher uma das opções do menu')
