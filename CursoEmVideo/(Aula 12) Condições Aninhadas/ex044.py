preço = float(input('Preço das compras: R$'))
escolha = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão
Qual o metodo de pagamento? '''))
if escolha <= 4:
    print('O valor da compra é R${:.2f}'.format(preço), end='. ')
    if escolha == 1:
        print('Você tem direito a 10% de dosconto, o preço a pagar é R${:.2f}'.format(preço * 0.9))
    elif escolha == 2:
        print('Você tem direito a 5% de desconto, o preço a pagar é R${:.2f}'.format(preço * 0.95))
    elif escolha == 3:
        print('Você não tem direito a disconto, o preço a pagar de cada parcela é é R${:.2f}'.format(preço / 2))
    else:
        son = input('Será cobrado um juros de 20% na sua compra...\nDigite "y" para proceguir ou qualquer tecla para sair ').upper()
        if son == 'Y':
            parcelas = int(input('Em quantas vezes deseja parcelar? (máximo 12 parcelas) '))
            print('o preço a pagar de cada parcela é é R${:.2f}'.format(preço * 1.2 / parcelas))
        else:
            print('Operação finalizada!')
else:
    print('Escolha uma opção entre 1, 2, 3 e 4...')
