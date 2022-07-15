#1° Jeito (sem import!!)
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
'''hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

# 2° Jeito
from math import hypot
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
