# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
# porção inteira. Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

from math import floor
n = float(input('Digite um número: '))

r = floor(n)

print('O número \033[4m{}\033[m tem a parte inteira \033[43m{}\033[m'.format(n,r))