'''from random import randint
print('{:=^50}'.format(' Bem vindo (a)'))
jogador = int(input('Vamos jogar Jokenpô!! Escolha uma opção: \n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\n'))
escolha = ('Pedra', 'Papel', 'Tesoura')
ia = randint(0, 2)
if jogador == 1 and ia == 2:
    print('Parabéns, você me venceu. Escolhi {}.!!'.format(escolha[ia]))
elif jogador == 1 and ia == 1:
    print('Você perdeu, escolhi {}.!!'.format(escolha[ia]))
elif jogador == 1 and ia == 0:
    print('Empatamos, também escolhi {}.!!'.format(escolha[ia]))
elif jogador == 2 and ia == 2:
    print('Você perdeu, escolhi {}.'.format(escolha[ia]))
elif jogador == 2 and ia == 1:
    print('Empatamos, também escolhi {}.'.format(escolha[ia]))
elif jogador == 2 and ia == 0:
    print('Parabéns, Você ganhou. Escolhi {}.'.format(escolha[ia]))
elif jogador == 3 and ia == 2:
    print('Empatamos, também escolhi {}.'.format(escolha[ia]))
elif jogador == 3 and ia == 1:
    print('Parabéns, Você ganhou. Escolhi {}.'.format(escolha[ia]))
elif jogador == 3 and ia == 0:
    print('Você perdeu, Escolhi {}.'.format(escolha[ia]))
else:
    print('Entrada Inválida!!')'''

#Professor
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')