'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

entrada = 0
while entrada != 5:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    entrada = int(input('O que deseja fazer com os valores: \n[ 1 ] Somar\n[ 2 ] Multplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n'))
    if entrada == 1:
        soma = n1 + n2
        print('O valor da soma foi: {}.'.format(soma))
    elif entrada == 2:
        mult = n1 * n2
        print('O resultado da multiplicação foi: {}.'.format(mult))
    elif entrada == 3:
        if n1 > n2:
            maior = n1
            print('O número maior digitado foi: {}.'.format(maior))
        else:
            maior = n2
            print('O maior número digitado foi: {}.'.format(maior))
    elif entrada == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        entrada = int(input('O que deseja fazer com os valores: \n[ 1 ] Somar\n[ 2 ] Multplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n'))
    elif entrada == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Volte quando quiser!!')

#Professor
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior: n2
        print('Entr {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
            print('Informe os números novamente: ')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte Sempre!')

