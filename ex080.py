'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

'''números = list()
for n in range(0, 5):
    puta = int(input('Digite um número: '))
    if n == 0:
        números.append(puta)
    for i, v in enumerate(números):
        if v >= números[n]:
            números.append(-1)
print(números)'''

def bubble_sort(v):
    fim = len(v)
    while fim > 0:
        i = 0
        while i < fim - 1:
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
            i += 1
        fim -= 1
    return v


listaNumeros = list()
for c in range(1, 6):
    listaNumeros.append(int(input(f'Digite o {c}º valor: ')))

print(bubble_sort(listaNumeros))

#professor
lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista... ')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista... ')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
























