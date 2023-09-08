"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

print(f'\n{"-" * 40}'
      f'\n{"LISTAGEM DE PREÇOS":^40}'
      f'\n{"-" * 40}')

produtos = ('Lápis', 1.75,
            'Borraca', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print(f'\n{"Produto":.<30}{"Preço"}')

for item in range(0, len(produtos), 2):
    print(f'{produtos[item]:.<30}R$ {produtos[item + 1]:.2f}')
