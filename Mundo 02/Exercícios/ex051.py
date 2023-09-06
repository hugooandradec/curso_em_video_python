"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão."""

termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))

for c in range(0, 10):
    pa = termo + (c * razão)
    print(f'O {c + 1}º termo da PA é: {pa}')
