def notas(*n, sit=False):
    """-> Função para analizar notas de varios alunos"""

    nota = dict()
    nota['total'] = len(n)
    nota['maior'] = max(n)
    nota['menor'] = min(n)
    nota['média'] = sum(n)/len(n)
    if sit:
        if nota['média'] > 7:
            nota['situação'] = 'BOA'
        elif nota['média'] < 6:
            nota['situação'] = 'RUIM'
        else:
            nota['situação'] = 'RAZOÁVEL'
    return nota


resp = notas(3, 4, 5, sit=True)
print(resp)
