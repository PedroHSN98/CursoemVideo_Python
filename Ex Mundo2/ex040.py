nota1 = float(input('Primeira nota: ')) 
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.2f} e {nota2:.2f}, a media do aluno é {media:.2f}')
if 7 > media >= 5:
    print('O aluno esta de Recuperação!')
elif media < 5:
    print('O aluno esta REPROVADO')
elif media >=7:
    print('O aluno esta APROVADO!')