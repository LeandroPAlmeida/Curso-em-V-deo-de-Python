'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
'''n = 'R$ 1'
n1 = 'R$ 10'
n2 = 'R$ 20'
n3 = 'R$ 50'
while True:
    us = int(input('Quanto gostaria de sacar: R$'))
    inteira = us // 50
    total = us - (inteira * 50)
    if total == 0:
        print(f'O valor R${us} será retirado em {inteira} em cédulas de {n3}.')
        break
    else:
        inteira1 = total // 20
        total = total - (inteira1 * 20)
        if total == 0:
            print(f'O valor R${us} será retirado em {inteira} em cédulas de {n3} e {inteira1} de {n2}.')
            break
        else:
            inteira2 = total // 10
            total = total - (inteira2 * 10)
            if total == 0:
                print(f'O valor R${us} será retirado em {inteira} em cédulas de {n3}, {inteira1} de {n2} e {inteira2} de {n1}.')
                break
            else:
                inteira3 = total // 1
                total = total - (inteira3 * 1)
                print(f'O valor R${us} será retirado em {inteira} em cédulas de {n3}, {inteira1} de {n2}, {inteira2} de {n1} e {inteira3} de {n}.')
                break'''

#Professor
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


