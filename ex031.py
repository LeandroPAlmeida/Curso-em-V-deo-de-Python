'''distância = int(input('Digite a distância da sua viagem em Km: '))
if distância <= 200:
    custo = distância * 0.50
    print('Com base na distância digitada, sua viagem custará: R${:.2f}.'.format(custo))
else:
    cust = distância * 0.45
    print('Com base na distância digitada, sua viagem custará: R${:.2f}.'.format(cust))'''
#Professor F1
'''distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:<2f}'.format(preço))'''

#Professor F2
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:<2f}'.format(preço))
