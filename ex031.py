km = float(input('Qual é a distância da sua viagem?: '))

print('Você está prestes a começar uma viagem de {}Km'.format(km))

if km < 200:
    preco = km * 0.5
else:
    preco = km * 0.45

print('O preço da sua passagem será de R${:.2f}'.format(preco))
