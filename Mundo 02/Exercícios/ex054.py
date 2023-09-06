"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores."""

from datetime import date

cont_menor_idade = 0
cont_maior_idade = 0
ano_atual = date.today().year

for pess in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {pess}º pessoa nasceu?: '))
    idade = ano_atual - ano_nascimento

    if idade < 21:
        cont_menor_idade += 1
    else:
        cont_maior_idade += 1

print(f'\n{cont_menor_idade} pessoas menores de idade.\n'
      f'{cont_maior_idade} pessoas maiores de idade.')
