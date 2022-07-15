p = float(input('Digite o preço do produto: R$'))
dp = p - (p * 5/100)
print('Com o desconto de 5% sobre valor de R${:.2f}, você só irá pagar R${:.2f}'.format(p, dp))
