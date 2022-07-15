qt = int(input('Por quantos dias você alugou o veiculo? '))
km = float(input('Quantos Km rodados: '))
pagar = (qt * 60) + (km * 0.15)
#rodado = km * 0.15
print('Valor total a pagar: R${:.2f}'.format(pagar))
