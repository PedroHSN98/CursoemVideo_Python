num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua escolha: '))

if opcao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido em HEXADECIMAL é igual a {hex(num)[2:]}')

else:
    print('Você não colocou nenhuma alternativa.')