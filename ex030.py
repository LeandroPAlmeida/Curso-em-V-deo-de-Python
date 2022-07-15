'''n = int(input('Digite um número inteiro: '))
n1 = n % 2
if n1 == 1:
    print('O número que você digitou é ímpar!')
else:
    print('O número que você digitou é par!')'''
#Professor
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))