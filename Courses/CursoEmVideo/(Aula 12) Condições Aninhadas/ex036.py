casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = float(input('Digite em quantos anos deseja pagar a casa: '))
emprestimo = casa/anos/12
if emprestimo > 0.3 * salario:
    print('''Infelizmente o emprestimo será negado.
Seu salario não condiz com o valor mínimo para emprestimo do imovel
Salario = R${:.2f}
Salaraio necessário R${:.2f}'''.format(salario, emprestimo*10/3))
else:
    print('Você tem direito ao emprestimo. \n O valor do emprestimo é de R${:.2f} por mes'.format(emprestimo))
    conf = input('Deseja prosseguir? [y/n] ').upper()
    if conf == 'N':
        print('Operação finalizada')
    else:
        print('Emprestimo realizado. Parabens!')
