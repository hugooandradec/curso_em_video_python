"""Faça um programa que leie o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Qual o peso da {p} pessoa? (kg): '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior:.2f}kg.')
print(f'O menor peso é {menor:.2f}kg.')
