from random import choice

primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
escolhido = choice(lista)

print('O escolhido foi {}'.format(escolhido))