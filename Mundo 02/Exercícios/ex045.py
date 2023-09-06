"""Crie um programa que faça o computador jogar Jokenpô com você"""

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('Escolha uma das opções abaixo, digitando o número correspondente:\n'
      '[0] - Pedra\n'
      '[1] - Papel\n'
      '[2] - Tesoura')
user = int(input('Qual opção você escolhe?: '))


print(f'\nVOCÊ JOGOU: {itens[user]}\n'
      f'EU JOGUEI: {itens[pc]}!')

if pc == 0: #PC JOGOU PEDRA
    if user == 0:
        print('EMPATAMOS!')
    elif user == 1:
        print('VOCÊ GANHOU!')
    elif user == 2:
        print('VOCÊ PERDEU!')

elif pc == 1: #PC JOGOU PAPEL
    if user == 0:
        print('VOCÊ PERDEU!')
    elif user == 1:
        print('EMPATAMOS!')
    elif user == 2:
        print('VOCÊ GANHOU')

elif pc == 2: #PC JOGOU TESOURA
    if user == 0:
        print('VOCÊ GANHOU!')
    elif user == 1:
        print('VOCÊ PERDEU!')
    elif user == 2:
        print('EMPATAMOS!')
