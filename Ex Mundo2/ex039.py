from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos de {atual}')
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18 - idade:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para o alistamento ')
elif idade > 18:
    saldo = idade - 18
    print(f'Você ja deveria ter se alistado ha {saldo} anos')