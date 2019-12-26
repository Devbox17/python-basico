"""
tempo = int(input('Quantos anos tem seu carro?: '))

if tempo <= 3:
    print('Carro Novo!')
else:
    print('Carro Velho!')
print('--FIM--')

# Outra forma de usar condição!

tempo = int(input('Quantos anos tem seu carro?: '))

print('Carro Novo!' if tempo <= 3 else 'Carro Velho!')

print('--FIM--')

nome = str(input('Qual é o seu nome?: '))

if nome == 'Andre':
    print('Que nome lindo você tem!')
else:
    print('Que nome feio você tem!')

print('Bom Dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua nota foi {:.1f}'.format(m))

if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

"""

# Outra forma condição simplificada

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua nota foi {:.1f}'.format(m))

print('Sua média foi boa! PARABÉNS!' if m >= 6 else 'Sua média foi ruim! ESTUDE MAIS!')