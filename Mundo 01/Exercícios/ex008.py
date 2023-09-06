"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros"""

mt = float(input('Digite a metragem a ser convertida: '))
cm = mt * 100
mm = mt * 1000

print(f'Você digitou {mt:.2f} metros.\n'
      f'{mt:.2f} metros equivale a {cm:.0f} centímetros.\n'
      f'{mt:.2f} metros equivale a {mm:.0f} milímetros.')
