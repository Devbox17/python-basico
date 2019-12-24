dias = int(input('Quantos dias alugados?: '))
km = float(input('Quantos Km rodados?: '))
taxac = 60
taxakm = 0.15
pagamento = (dias * taxac) + (km * taxakm)

print('O total a pagar é de R${}'.format(pagamento))