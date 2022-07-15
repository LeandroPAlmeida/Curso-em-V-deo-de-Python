'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8 '''

print('Sequência de Fibonacci')
t = int(input('Quantos termos deseja ver: '))
n = 0
fn = 1
c = 1
print('{} -> {} -> '.format(n, fn), end='')
result = n + fn
while c < t:
    result2 = fn + result
    print('{} -> '.format(result2), end='')
    fn = result
    result = result2
    c += 1
print('Acabou!!')

#Professor
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
    print(' -> FIM')
    print('~'*30)
