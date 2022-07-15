'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
print('Bem - Vindo(a)')
nascimento = int(input('Digite o ano que você nasceu, para análisarmos se você deve/não se alistar neste ano: '))
mulher = str(input('Digite seu sexo: \n[ M ] - Masculino\n[ F ] Feminino\n')).upper()
ano = date.today().year
idade = ano - nascimento
if mulher == 'F':
    print('Mulheres não precisam se alistar no Serviço Militar!!')
elif mulher == 'M':
    if idade < 18:
        falta = 18 - idade
        print('Ainda não chegou a sua hora. Faltam {} anos, fique atento!! \nSeu alistamento será em {}.'.format(falta, (falta + ano)))
    elif idade == 18:
        print('Sua hora chegou, SE ALISTE JÁ!!')
    elif idade > 18:
        falta = idade - 18
        print('Você já deveria ter se alistado à {} anos atrás, corra para a Diretoria de Serviço Militar mais próxima!!'.format(falta))
else:
    print('Entrada inválida. Tente novamente.')


#Professor
'''from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = idade - 18
    print('Ainda faltam {} anos para o alsitamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))'''