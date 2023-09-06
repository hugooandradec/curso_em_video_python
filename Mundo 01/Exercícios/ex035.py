"""Desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem ou não formar um triângulo."""

a = float(input('Digite o comprimento do primeiro segmento: '))
b = float(input('Digite o comprimento do segundo segmento: '))
c = float(input('Digite o comprimento do terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print(f'Com os comprimentos de {a:.2f}cm, {b:.2f}cm e {c:.2f}cm, podemos formar um triângulo.')
else:
    print(f'Com os comprimentos de {a:.2f}cm, {b:.2f}cm, {c:.2f}cm, não podemos formar um triângulo.')
