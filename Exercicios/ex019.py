# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
# programa que ajude ele, lendo o nome delas a escrevendo o nome do escolhido.

from random import choice

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]

esc = choice(lista)

print('\033[4;31mO aluno escolhido foi:{}'.format(esc))