import math
an = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o Seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tangente))
