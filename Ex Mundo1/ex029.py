# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual a velocidade atual do seu carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (v-80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')


