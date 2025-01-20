peso = float(input('Qual é o seu peso? (kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('Voce esta ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('Parabéns você esta na faixa de peso normal')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
    