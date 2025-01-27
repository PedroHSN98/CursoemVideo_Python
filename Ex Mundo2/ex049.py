'''
Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um faço for 
'''

num = int(input('Digite um número para ver a sua tabuada: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')