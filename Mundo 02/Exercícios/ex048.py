"""Faça um programa que calcule a soma entre todos os número ímpares que são múltiplos de 3 e que se encontram
no intervalo de 1 até 500."""

soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é de {soma}')
