'''
Faça um programa que leia a largura e a altura de uma parede em mestros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²
'''

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e a sua área é de {area}m²')

tinta = area / 2

print(f'Para pintar essa parede, você precisara de {tinta}l de tinta')