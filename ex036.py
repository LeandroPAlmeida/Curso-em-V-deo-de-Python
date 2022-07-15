'''print('Vamos avaliar seu empréstimo!!')
vc = float(input('Qual o valor da casa/propriedade? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
pres = (vc / (anos * 12)) 
minimo = salário * 30 / 100
if pres <= minimo:
    print('Seu emprestimo foi aceito!!')
else:
    print('Seu emprestimo foi recusado!!')'''

#Professor
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='') # (end='') para prestação ficar na mesma linha!!
print(' a prestação será de R${:.2f}.'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

