"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o"""

soma = 0
cont = 0
for c in range(0, 6):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'\nVocê digitou {cont} número(s) PAR(ES) e a soma foi {soma}.')
