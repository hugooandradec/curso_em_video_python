"""Crie um programa que leie o nome e preço de vários produtos. O programa deverá perguntar se o usuário quer continuar.
No final, mostre:
1 - Qual o total gasto na compra
2 - Quantos produtos custam mais de R$ 1.000
3 - Qual é o nome do produto mais barato."""

valor_total = cont_mil = cont_prod = valor_prod_barato = 0
nome_prod_barato = ' '

print('\nLOJAS MIL GRAU\n')

while True:
    produto = str(input('Nome do produto: ')).upper().strip()
    preco = float(input('Valor do produto: R$'))
    cont_prod += 1
    valor_total += preco

    if preco > 1000:
        cont_mil += 1

    if cont_prod == 1 or preco < valor_prod_barato:
        valor_prod_barato = preco
        nome_prod_barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S]/[N]: ')).upper().strip()
    if resp == 'N':
        break

print(f'\nA quantidade de produtos foi de: {cont_prod}.\n'
      f'Total gasto na compra foi de R${valor_total:.2f}.\n'
      f'Total de produtos que custam mais de R$1000: {cont_mil}.\n'
      f'O produto mais barato foi {nome_prod_barato}, com o valor de R${valor_prod_barato:.2f}')
