frase = input('Digite seu nome completo: ').strip()

print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(frase.upper()))
print('Seu nome em minúsculas é {}'.format(frase.lower()))
print('Seu nome tem ao todo {} letras'.format(len(frase) - frase.count(' ')))
separa = frase.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))