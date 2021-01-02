import random
nome1 = input('digite o nome do aluno 1:')
nome2 = input('digite o nome do aluno 2:')
nome3 = input('digite o nome do aluno 3:')
nome4 = input('digite o nome do aluno 4:')
lista = [nome1, nome2, nome3, nome4]
print('o aluno escolhido foi:', random.choice(lista))
