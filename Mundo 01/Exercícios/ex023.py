"""Faça um programa que leia um número de 0 até 9999 e mostre na tela cada um dos dígitos separados em unidade, dezena
centena e milhar"""

n = int(input('Digite um número entre 0 e 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'O número digitado foi {n}\n'
      f'A sua unidade é: {u}\n'
      f'A sua dezena é: {d}\n'
      f'A sua centena é: {c}\n'
      f'O seu milhar é: {m}')
