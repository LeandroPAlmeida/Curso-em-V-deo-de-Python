'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

'''from math import factorial
número = int(input('Digite um número para efetuar seu fatorial: '))
calculo = factorial(número)
print('O fatorial de {} é {}.'.format(número, calculo))'''

#Professor #1
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

#2

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculamdo {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-= 1
print('{}'.format(f))