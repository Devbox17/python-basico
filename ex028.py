# Jogo da Adivinhação v1.0

from random import randint
from time import sleep

comp = randint(0, 5) # Faz o computador "PENSAR"

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-' * 20)

jog = int(input('Em que número eu pensei?: '))

print('PROCESSANDO...')
sleep(1)

if jog == comp:
    print('PARABÉNS!!! Você conseguiu me vencer!')
else:
    print('GANHEI!!! Eu pensei no número {} e você no {}'.format(comp, jog))
