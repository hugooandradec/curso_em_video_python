"""Faça um programa que leia 3 números e mostre qual é o MAIOR e qual é o MENOR"""

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print(f'O maior número é o: {maior:.0f}\n'
      f'O menor número é o: {menor:.0f}')
