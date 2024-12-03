preco = float(input('Qual é o preço do produto ? R$: '))
novo = preco - (preco * 5 / 100)  # Calcula o preço final subtraindo o desconto
print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${novo}')
