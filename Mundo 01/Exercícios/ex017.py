"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa"""

from math import hypot

cat_ops = float(input('Qual o comprimento do cateto oposto?: '))
cat_adj = float(input('Qual o comprimento do cateto adjacente?: '))
hip = hypot(cat_ops, cat_adj)

print(f'O comprimento da hipotenusa é de {hip:.2f}!')
