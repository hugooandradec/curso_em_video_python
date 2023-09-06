"""Crie um programa que simula o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('=' * 30)
print(f'{"BANCO MIL GRAU!!":^30}')
print('=' * 30)

cédula50 = cédula20 = cédula10 = cédula1 = 0

saque = int(input('\nQual valor deseja sacar?: R$ '))

while True:
    if saque > 0:
        cédula50 = int(saque / 50)
        saque -= cédula50 * 50
        if cédula50 > 0:
            print(f'Você receberá {cédula50} nota(s) de R$50.')
    if saque > 0:
        cédula20 = int(saque / 20)
        saque -= cédula20 * 20
        if cédula20 > 0:
            print(f'Você receberá {cédula20} nota(s) de R$20.')
    if saque > 0:
        cédula10 = int(saque / 10)
        saque -= cédula10 * 10
        if cédula10 > 0:
            print(f'Você receberá {cédula10} nota(s) de R$10.')
    if saque > 0:
        cédula1 = int(saque / 1)
        saque -= cédula1 * 1
        if cédula1 > 0:
            print(f'Você receberá {cédula1} nota(s) de R$1.')
    elif saque == 0:
        break
print('\nTENHA UM ÓTIMO DIA!!')
