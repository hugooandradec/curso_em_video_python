"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'"""

cidade = str(input('Digite o nome da cidade que você mora: ')).strip().title()

cidade_separada = cidade.split()

print(f'A cidade começa com o nome "Santo"?: {"Santo" in cidade_separada[0]} ')
