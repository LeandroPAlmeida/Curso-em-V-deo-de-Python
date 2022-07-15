'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Me diga uma frase: ')).strip().upper()
fsplit = frase.split()
fjoin = ''.join(fsplit)
inverso = ''
for letras in range(len(fjoin) -1, -1, -1):
    inverso += fjoin[letras]
print('A frase digitada ao contrário ficou: {}.'.format(inverso))
if fjoin == inverso:
    print('A frase {} é um políndromo!!'.format(frase))
else:
    print('A frase digitada não é um políndromo!!')

#Professor
'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' #Conexão [1/3]
#inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, - 1): #Conexão [2/3]
    inverso += junto[letra]   #Conexão [3/3]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''





