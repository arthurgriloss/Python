sexo = input('Informe o seu sexo. \nDigite a tecla [ m ] para masculino ou a tecla [ f ] para feminino: ').strip().upper()
while sexo not in 'FM':
    print('!----- ERROR -----!')
    print('Tecla invalida, digite [ m ] para masculino e [ f ] para feminino')
    sexo = input('Informe o seu sexo. \nDigite a tecla [ m ] para masculino ou a tecla [ f ] para feminino: ').strip().upper()
if sexo == 'M':
    print('\nO senhor é muito elegante')
elif sexo == 'F':
    print('\nA senhora é a mais bela que ja vi')
