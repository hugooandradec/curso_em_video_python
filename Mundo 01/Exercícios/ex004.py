"""Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele"""

dado = input('Digite algo: ')
print(f'Você digitou: {dado}\n'
      f'O tipo primitivo é: {type(dado)}\n'
      f'Só tem espaços?: {dado.isspace()}\n'
      f'É um número?: {dado.isnumeric()}\n'
      f'É alfabético?: {dado.isalpha()}\n'
      f'É alfanumérico?: {dado.isalnum()}\n'
      f'Está em maiúsculas?: {dado.isupper()}\n'
      f'Está em minúsculas?: {dado.islower()}\n'
      f'Está capitalizada?: {dado.istitle()}')
