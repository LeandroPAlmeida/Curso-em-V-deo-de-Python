'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
today = date.today().year
menor = 0
maior = 0
for c in range(0, 7):
    pessoa = int(input('Digite o ano do seu nascimento: '))
    idade = today - pessoa
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas das sete que participaram não atingiram a maior idade e {} já são maiores.'.format(menor, maior))

#Professor
'''from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))'''