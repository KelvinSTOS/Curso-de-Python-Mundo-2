from time import sleep
from random import randint
print('-+-+-'*15)
print('BEM-VINDO(A) AO JOGO JOKENPÔ, DIVIRTA-SE!')
print('-+-+-'*15)
print('Olá, te desafio a me ganhar no Jokenpô!')
print('''Escolha o que vai jogar:
[0] Pedra
[1]Papel
[2]Tesoura''')
P1 = int(input('Escolha uma das opções: '))
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('JÓ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
if comp == 0:
    if P1 == 0:
        print('Empate, pedra com pedra vira muro meu chapa!')
    elif P1 == 1:
        print('Você me venceu, joguei pedra')
        print('~~ Jogador: Há, papel é mais forte!')
    elif P1 == 2:
        print('Ganhei! Pedra! Não vai mais poder usar essa tesoura tão cedo!')
        print('~~ Jogador: Droga! minha tesourinha ç.ç')
elif comp == 1:
    if P1 == 0:
        print('Papel Cobre a Pedra meu chapa, Perdeu!')
        print('~~ Jogador: Droga ç.ç Perdi, escolhi pedra')
    elif P1 == 1:
        print('Papel com Papel faz livro! Jogue de novo')
    elif P1 == 2:
        print('Perdi meu papel, você corta com sua tesourinha -,,.,-')
        print('~~ Jogador: Uma vitória contra as máquinas!')
elif comp == 2:
    if P1 == 0:
        print('Perdi, tirei tesoura')
    elif P1 == 1:
        print('Você perdeu tesoura picota papel!')
    elif P1 == 2:
        print('Tesoura, Tesoura, isso não vai longe! Vamos novamente')
