# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print(f'{i}', end=' ')
print(f'O número {num} foi divisível {tot} vezes')