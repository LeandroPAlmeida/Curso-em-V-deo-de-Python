'''salário = float(input('Digite seu salário: '))
if salário >= 1250:
    aumento = (salário * 10 / 100) + salário
    print('Você teve um aumento de 10%, seu salário agora é: R${:.2f}.'.format(aumento))
else:
    aumento = (salário * 15 / 100) + salário
    print('Você teve um aumento de 15%, seu salário agora é: R${:.2f}.'.format(aumento))'''

#Professor
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
