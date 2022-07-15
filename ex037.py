'''n = int(input('Digite um número inteiro: '))
opção = int(input('Digite a conversão desejada: \n[1] Binário \n[2] Octal \n[3] Hexadecimal\n '))

if opção == 1:
    print('O valor {} em binário é {}.'.format(n, bin(n)[2:]))
elif opção == 2:
    print('O valor {} em octal é {}.'.format(n, oct(n)[2:]))
elif opção == 3:
    print('O valor {} em hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente!!')'''

#Professor
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para coversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')

