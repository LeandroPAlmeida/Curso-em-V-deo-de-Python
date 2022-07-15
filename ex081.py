''''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

num = []
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Deseja adicionar mais algum número? [S/N] '))
    if r in 'Nn':
        break
print(f'A) {len(num)} digitados.')
num.sort(reverse=True)
print(f'B) {num}.')
if 5 in num:
    print(f'C) O valor 5 está na lista.')
else:
    print(f'C) O valor 5 não está na lista.')

#Professor
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foie ncontrado na lista.')
