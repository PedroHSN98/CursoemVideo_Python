#Crie Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input(print('Coloque o seu nome completo: '))

print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
print(len(nome))

primeiro_nome = nome.split()[0]
print(f'Número de letras no primeiro nome ({primeiro_nome}): {len(primeiro_nome)}')