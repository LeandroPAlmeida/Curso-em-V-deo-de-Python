'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço normal

– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' Lojas TOBEÔ '))
produto = float(input('Digit o valor do produto: R$'))
opção = int(input('[ 1 ] Á vista em Dinheiro / Cheque: 10% de DESCONTO!!\n[ 2 ] Á vista no cartão: 5% de DESCONTO!!\n[ 3 ] Em até 2x no cartão: Preço Normal!!\n[ 4 ] 3x ou mais no cartão: 20% de juros.\n'))
if opção == 1:
    print('O Preço com 10% de Desconto, ficará: R${:.2f}.'.format(produto - (produto * (10 / 100))))
elif opção == 2:
    print('O preço com 5% de Desconto, ficará: R${:.2f}.'.format((produto - (produto * (5 / 100)))))
elif opção == 3:
    print('Preço Total: R${:.2f}.'.format(produto))
elif opção == 4:
    parcelas = int(input('Quantas parcelas: '))
    totalparc = produto / parcelas
    print('O valor em {}x no cartão será R${:.2f}. Com valor total de R${:.2f}.'.format(parcelas, totalparc, produto + (produto * (20 / 100))))

#Professor
'''print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''#FORMAS DE PAGAMENTO
#[ 1 ] à vista dinheiro / cheque
#[ 2 ] à vista cartão
#[ 3 ] 2x no cartão
#[ 4 ] 3x ou mais no cartão''')
'''opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de Pagamento. Tente Novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))'''