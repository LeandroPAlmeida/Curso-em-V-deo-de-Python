'''velocidade = float(input('Digite sua velocidade: '))
if(velocidade > 80):
    multa = (velocidade - 80.0) * 7.00
    print('Você ultrapassou o limite permitido que é de 80 km/h e recebeu uma multa de: R${:.2f}'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Você não possui dispesas.')
    print('Tenha um bom dia! Dirija com segurança!')'''
#Professor
velocidad = float(input('Qual é a velocidade atual do carro? '))
if velocidad > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidad-80) * 7
    print('Você deve pagar um amulta de R${:.2f}!'.format((multa)))
print('Tenha um bom dia! Dirija com segurança!')