"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome"""

nome = str(input('Digite seu nome completo: ')).strip().title()

print(f'Seu nome contém o nome Silva?: {"Silva" in nome}')
