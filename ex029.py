vel = int(input('Qual é a velocidade atual do carro?: '))

if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO!!! Você excedeu o limite permitido que é de 80Km/h')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${}'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
