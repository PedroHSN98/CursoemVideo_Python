'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for Impar. Desconsidere
'''
soma = 0
for i in range(0, 6):
    n = int(input('Digite 6 numeros inteiros para serem somados: '))
    if n % 2 == 0:
        soma += n
    else:
        print(f'{n} é ímpar e foi desconsiderado.')

print(f'A soma dos números pares digitados é: {soma}')
