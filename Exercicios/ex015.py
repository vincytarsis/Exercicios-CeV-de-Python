# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

d = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

tp= d * 60 + km * 0.15

print('Preço a pagar:R$\033[7;34;41m{:.2f}\033[m'.format(tp))