from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade}')
if idade <=9:
    print('Classificação MIRIM')
elif idade <=14: 
    print('Classificação INFANTIL')
elif idade <= 25: 
    print('Classificação Junior')
else:
    print('Classificação Master')