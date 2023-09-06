"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto."""

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str((input('Qual o seu sexo? [M/F]: '))).strip().upper()

if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'

print(f'Seu sexo é {sexo}.')
