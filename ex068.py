'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random
par = 'par'
impar = 'impar'
lista = [par, impar]
comp = random.choice(lista)
compn = random.randrange(0, 5)
c = 0
while True:
    print('Vamos jogar Par ou Ímpar!!')
    n = int(input('Digite um número: '))
    j = str(input('Par / Ímpar !? ')).strip().lower()
    if j == par in comp == par:
        comp = impar
    elif j == impar in comp == impar:
        comp = par
    else:
        print('Entrada incorreta!! Tente novamente!!')
    soma = (n + compn) % 2
    if soma == 0:
        win = par
    else:
        win = impar
    if win == comp:
        vencedor = comp
        print('Eu ganhei!! :V')
        print(f'Você jogou {n} e o computador {compn}. Total de {n+compn} deu {win.upper()}')
        break
    else:
        vencedor = j
        c += 1
        print('Você venceu!!')
        print(f'Você jogou {n} e o computador {compn}. Total de {n+compn} deu {win.upper()}')
print(f'Vitórias consecutivas {c}.')

#Professor
'''from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper() [0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VocÊ VENCEU!')
            v += 1
        else:
            print('VocÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')'''
