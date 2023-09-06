"""Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela os 'n' primeiros elementos de uma
Sequência de Fibonacci."""

número = int(input('Quantos termos você quer mostrar?: '))
termo1 = 0
termo2 = 1

print(f'{termo1} - {termo2}', end=' ')
contador = 3

while contador <= número:
    termo3 = termo1 + termo2
    print(f'- {termo3}', end=' ')
    termo1 = termo2
    termo2 = termo3
    contador += 1

print('- FIM')
