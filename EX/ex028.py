from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "Pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Emque número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}!')
