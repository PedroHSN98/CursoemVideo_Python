nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro':
    print('Você tem o nome mais bonito do mundo!')
elif nome == 'Maria' or nome == 'Sandra':
    print('É um nome bem comum ')
elif nome in 'Ana Clara Maria Sofia':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia {nome}')