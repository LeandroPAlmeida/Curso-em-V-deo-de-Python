'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''


from random import randint
n = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(f'Os valores sorteados foram: {n}')
print(f'O maior valor sorteado foi o: N°{max(n)}.')
print(f'O menor valor sorteado foi o: N°{min(n)}.')

#Professor
from random import randint
números = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(números)}.')
print(f'O menor valor sorteado foi: {min(números)}.')