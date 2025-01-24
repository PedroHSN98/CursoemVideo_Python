'''
Faça um programa que mostre na tela 
uma contagem regressiva para o estouro de
 fogos de artificio, indo de 10 ate 0, com
 uma pausa de 1s entre elas
'''
import time
for i in range(10, -1, -1):
    time.sleep(1)
    print(i)
print('(-BOM-)')