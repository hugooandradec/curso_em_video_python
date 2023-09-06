"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto"""

valor = float(input('Qual o valor do produto? R$ '))
desc = valor - valor * 5 / 100

print(f'O valor do produto é de R$ {valor:.2f};\n'
      f'Com o desconto de 5% o novo valor será de R$ {desc:.2f}.')


"""
inicial = float(input('Digite o valor antigo: R$ '))
novo = float(input('Digite o valor novo: R$ '))
total = (novo - inicial) / inicial * 100

print(f'A diferença entre R$ {inicial:.2f} e R$ {novo:.2f}, é de {total:.2f}%')
"""