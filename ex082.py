'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

num = []
par = []
imp = []
while True:
    v = (int(input('Digite um número: ')))
    if v % 2 == 0:
        num.append(v)
        par.append(v)
    else:
        num.append(v)
        imp.append(v)
    resp = str(input('Deseja adicionar outro número: [S/N] '))
    if resp in 'Nn':
        break
print(f'Todos os números adicionados: {num}.')
print(f'Pares: {par}.')
print(f'Ímpares: {imp}.')

#Professor
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lsista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')


















