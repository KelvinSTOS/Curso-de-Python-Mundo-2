'''ano = int(input('Em que ano você nasceu?'))
idade = ano - 2024
if ano <= 18:
    print('Você ainda tem {} anos, e  não está na idade, volte quando completar os 18 Anos!'.format(idade))
elif:
    print('Você já tem {} ano e já pode se alista GUERREIRO!'.format(idade))'''
    
#Ou dessa forma!
from datetime import date
hoje = date.today().year
nasc = int(input('Em que ano você nasceu?'))
idade = hoje - nasc
print('Você possui {} Anos nesse ano de {} nascido em {}'.format(idade, hoje, nasc))
if idade == 18:
    print('Você já tem {} e pode se ALISTAR!!'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} Anos para você se alistar!'.format(saldo))
    ano = hoje + saldo
    print('Seu alistamento será no ano de {}.'.format(ano))
elif nasc > 18:
    saldo = idade - 18
    ano = saldo + idade
    print('Seu alistamento deveria ter sido em {} ano!'.format(ano))
    print('Você deveria ter se alistado há {} Ano.'.format(saldo))
