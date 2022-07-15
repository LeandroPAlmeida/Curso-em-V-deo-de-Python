'''Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep

import emoji

'''print('10')
sleep(1)
print('9')
sleep(1)
print('8')
sleep(1)
print('7')
sleep(1)
print('6')
sleep(1)
print('5')
sleep(1)
print('4')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print(emoji.emojize('Gime a White Mocha!! :smiling_face_with_sunglasses:'))'''

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print(emoji.emojize('Zero Absoluto!! :ice:'))

#Professor
'''from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOW!')'''

