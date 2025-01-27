'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for Impar. Desconsidere
'''
soma = 0
cont = 0 
for i in range(1, 7):
    num = int(input(f'Digite o {i} valor: '))
    soma += num
    cont += 1
print(f'Você informou {cont} números e a soma foi {soma}')
