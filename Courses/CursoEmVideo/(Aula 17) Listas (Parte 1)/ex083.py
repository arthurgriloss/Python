exp = input('Digite sua expressão: ')
pilha = list()
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão esta correta')
else:
    print('sua expressao esta incorreta')