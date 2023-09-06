"""Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import choice

lista = list(range(11))
num_user = -1
num_pc = choice(lista)
cont_num = 0

while num_pc != num_user:
    num_user = int(input('Qual número você acha que escolhi, entre 0 e 10?: '))

    if num_pc != num_user and num_pc > num_user:
        cont_num += 1
        print(f'Você escolheu o número {num_user} e errou! Tente outra vez, um número maior...\n')
    elif num_pc != num_user and num_pc < num_user:
        cont_num += 1
        print(f'Você escolheu o número {num_user} e errou! Tente outra vez, um número menor...\n')

print(f'Você escolheu o número {num_user} e eu escolhi o número {num_pc}.\n'
      f'Parabéns, você acertou na {cont_num + 1}ª tentativa!')
