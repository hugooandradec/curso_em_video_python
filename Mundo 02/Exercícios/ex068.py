"""Faça um programa que jogue par ou ímpar com o computador. O jogo só sera interrompido, quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

user_vit = pc_vit = 0
print('Vamos jogar PAR ou ÍMPAR\n')

while True:
    user = int(input('Qual número você escolhe, entre 0 e 10?: '))
    pc = randint(0, 10)
    total = user + pc
    op = ' '
    while op not in 'PI':
        op = str(input('[P] ou [I]? ')).upper()

    if total % 2 == 0 and op in 'P':
        user_vit += 1
        print(f'Eu escolhi {pc} e você escolheu {user}\n'
              f'O total é de {total}\n'
              'Você ganhou! Vamos de novo.')

    elif total % 2 == 1 and op in 'I':
        user_vit += 1
        print(f'Eu escolhi {pc} e você escolheu {user}\n'
              f'O total é de {total}\n'
              'Você ganhou! Vamos de novo.')

    else:
        pc_vit += 1
        print(f'Eu escolhi {pc} e você escolheu {user}\n'
              f'O total é de {total}\n'
              f'Eu ganhei!\n'
              f'Você ganhou {user_vit} vezes consecutivas!')
        if pc_vit == 1:
            break
