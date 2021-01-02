salario = float(input('Digite o salário do funcionario: '))
nSalario = salario * 1.1 if salario > 1250 else salario * 1.15
print('O funcionário ganhava R${:.2f} novo salário é R${:.2f}'.format(salario, nSalario))
