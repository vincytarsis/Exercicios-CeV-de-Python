""" Elabore um programa que calcule o calor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento: -À vista dinheiro/cheque: 10% de desconto; -À vista no cartão: 5% de desconto; -Em até 2x no cartão: preço
normal; -3x ou mais vezes: 20% de juros; """

pr = float(input('Preço:R$:'))
pg = int(input('Pagamento:\n(1)À vista dinheiro/cheque\n(2)À vista no cartão\n(3)Em até 2x no cartão\n(4)Em 3x ou mais\n'))

if pg == 1:
    print('10% de desconto:R${:.2f}'.format(pr - (pr * 0.1)))
elif pg == 2:
    print('5% de desconto:R${:.2f}'.format(pr - (pr * 0.05)))
elif pg == 3:
        print('Valor a paga: 2x {:.2f}'.format(pr / 2))
elif pg == 4:
    pc = int(input('Em quantas vezes: '))
    par = pr + (pr * 0.2)
    print('20% de juros:{}x de {:.2f} com o total de:R${:.2f}'.format(pc, par / pc, par))
else:
    print('\033[31mOpção invalida')
