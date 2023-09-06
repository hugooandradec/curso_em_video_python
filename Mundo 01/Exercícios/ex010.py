"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere o dólar no valor de $1.00 = R$ 3,27"""

real = float(input('Quanto de dinheiro você tem disponível? R$ '))
dol = real / 4.98

print(f'Você tem R${real} e pode comprar ${dol:.2f}.')
