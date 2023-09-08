"""Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostra a listagem
de números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint

numeros_aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end='')
for n in numeros_aleatorios:
    print(f'{n} ', end='')

print(f'\nO maior valor foi: {max(numeros_aleatorios)}\n'
      f'O menor valor foi: {min(numeros_aleatorios)}')
