"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem contar os espaços)
Quantas letras tem o primeiro nome."""

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em maiúsculo: {nome.upper()} ')
print(f'Seu nome em minúsculo: {nome.lower()}')
print(f'Quantidade de letras em seu nome: {len(nome.replace(" ", ""))}')
print(f'Quantidade de letras em seu primeiro nome: {len(nome.split()[0])}')
