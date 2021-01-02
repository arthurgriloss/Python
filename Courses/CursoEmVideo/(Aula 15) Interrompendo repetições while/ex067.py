while True:
    n = int(input('Dgite o número o qual deseja saber a tabuada: '))
    if n < 0:
        break
    print('='*10)
    for c in range(0,10):
        print(f'{n} x {c+1} = {n*(c+1)}')
    print('=' * 10)
print('Programa da tabuada encerrado!')