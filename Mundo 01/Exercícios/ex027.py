"""Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente"""

nome = str(input('Digite seu nome completo: ')).strip().title()

print(f'Seu primeiro nome é: {nome.split()[0]}\n'
      f'Seu último nome é: {nome.split()[-1]}')
