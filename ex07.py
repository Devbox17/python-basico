n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2

print('A média entre {} e {} é igual a {:.1f}'.format(n1, n2, media))

# Quando você usa : nas chaves, indica para o python que você quer aumentar ou diminuir as casas visíveis.

# Usando :2f é diferente de :.2f fazem coisas diferentes.