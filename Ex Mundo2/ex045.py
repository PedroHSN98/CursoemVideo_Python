# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    ''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 12)
print(f'Computador escolheu {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 12)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:  
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')

elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:  
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')


elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
          print('EMPATE')
    else:
        print('JOGADA INVALIDA!')