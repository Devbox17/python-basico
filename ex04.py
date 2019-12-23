palavra = input('Escreva algo: ')
print('O tipo primitivo desse valor é {}'.format(type(palavra)))
print('Só tem espaços? {}'.format(palavra.isupper))
print('É um número? {}'.format(bool(palavra)))
