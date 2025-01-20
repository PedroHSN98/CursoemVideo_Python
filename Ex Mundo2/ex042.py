r1 = float(input('Primeiro segmeneto: '))
r2 = float(input('Primeiro segmeneto: '))
r3 = float(input('Primeiro segmeneto: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acim NÃO PODEM FORMAR triangulo')