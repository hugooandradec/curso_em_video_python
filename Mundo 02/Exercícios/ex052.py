"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input('Digite um número inteiro, acima de 1, para saber se ele é PRIMO ou não: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1

if tot == 2:
    print(f'O número {num} foi divisível {tot}x e é primo!')
else:
    print(f'O número {num} foi divisível {tot}x e não é primo!')
