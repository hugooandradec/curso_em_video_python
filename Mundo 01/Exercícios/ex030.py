"""Crie um programa que leia um número na tela e mostre se ele é PAR ou ÍMPAR."""

num = int(input('Digite um número inteiro: '))

print(f'Você digitou o número {num}.\n')

if num % 2 == 0:
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é ÍMPAR!')
