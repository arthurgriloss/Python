distancia = float(input('Quero te ajuda a achar o preço da sua passagem \nPor favor digite a distancia em quilometros:'))
if distancia > 200:
    print('Você tem direito ao nosso valor promocional! \n O preço da sua passagem é R${:.2f}'.format(distancia*0.45))
else:
    print('O preço da sua passagem é R${:.2f}'.format(distancia*0.50))