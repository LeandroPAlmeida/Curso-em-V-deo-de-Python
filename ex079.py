'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v in valores:
        print('Valor repetido não adicionado!!')
    else:
        valores.append(v)
        print('Valor adicionado com sucesso!!')
    r = str(input('Quer adicionar mais valores!? [S/N] '))
    if r in 'Nn':
        break
print('*=' * 30)
valores.sort()
print(valores)

#Professor
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')