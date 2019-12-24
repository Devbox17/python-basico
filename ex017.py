import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjascente: '))
h = math.hypot(co, ca)

#h = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))

print('A hipotenusa vai medir {:.2f}'.format(h))