distancia = float(input('Qual é a distancia da sua viagem? '))
print(f'Você esta prester a começar uma viagem de {distancia}')

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'E o preço da sua passagem será de RS${preco:.2f}')
