"""Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário acertou ou errou."""

from random import choice

lista = [0, 1, 2, 3, 4, 5]
num_pc = choice(lista)

num_user = int(input('Qual número você acha que o PC escolheu, entre 0 e 5?: '))
print(f'Você escolheu o número {num_user} e eu escolhi o número {num_pc}')

if num_pc == num_user:
    print('Parabéns, você acertou!')
else:
    print('Você errou! Tente outra vez.')
