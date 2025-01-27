'''
Faça um programa que calcule a soma 
entre todos os numeros impares que sao
 multiplos de 3 e que se encontram no 
 intervalo de 1 ate 500
'''

cont = 0 
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i
print(f'A soma de todos os {cont} valores solicitados é {soma}')