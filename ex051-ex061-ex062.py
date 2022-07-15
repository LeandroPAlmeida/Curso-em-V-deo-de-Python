'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

from time import sleep

#Ex51
'''t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(1, 11):
    pa = t + (c - 1) * r
    print('A progressão aritmética do {}° termo {} e a razão {} é: {}'.format(c, t, r, pa))'''

#Ex61
'''t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c < 10:
    pa = t + (c - 1) * r
    c += 1
    print("A progressão aritmética do {}° termo {} e a razão {} é: {}.".format(c, t, r, pa))'''

#Ex62
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
termos = 0
tm = 10
while tm != 0:
    termos = termos + mais
    while c <= termos:
        print('{} -> '.format(t), end='')
        t += 1
        c += 1
    mais = int((input('Quantos termos você quer mostrar a mais? ')))
print('Progressão finalizada com {} termos mostrados!'.format(termos))



#Professor
'''primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' ->')
print('ACABOU')'''

#Ex61
'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += 1
    cont += 1
print('FIM')'''

#Ex062
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))