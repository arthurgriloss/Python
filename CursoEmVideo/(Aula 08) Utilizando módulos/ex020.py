from random import shuffle
n1 = input('digite o nome do aluno 1:')
n2 = input('digite o nome do aluno 2:')
n3 = input('digite o nome do aluno 3:')
n4 = input('digite o nome do aluno 4:')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem de apresentação é:\n', lista)
