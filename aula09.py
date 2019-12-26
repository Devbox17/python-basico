frase = 'Curso em Vídeo Python'

# Fatiamento

print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print()

# Análise

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

print()

# Transformação 

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

print()

frasedois = '   Aprenda Python  '

print(frasedois)
print(frasedois.strip())
print(frasedois.rstrip())
print(frasedois.lstrip())

print()

# Divisão

print(frase.split())

print()

# Junção

print('-'.join(frase))