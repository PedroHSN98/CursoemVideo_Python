n1 = int(input(print('Coloque o primerio número')))
n2 = int(input(print('Coloque o segundo número: ')))

if n1 > n2:
    print(f'O primeiro número {n1} é maior que o segundo número {n2}')
elif n2 > n1: 
    print(f'O segundo número {n2} é maior que o primeiro número {n1}')
elif n1 == n2 and n2 == n1:
    print('Os dois numeros são iguais, por isso não tem um maior que o outro') 

else:
    print('Algo deu etrado!')

