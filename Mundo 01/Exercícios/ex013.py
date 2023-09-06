"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento."""

valor = float(input('Qual o salário atual do funcionário?: R$ '))
aum = valor + valor * 15 / 100

print(f'O salário do funcionário era de R$ {valor:.2f}\n'
      f'E agora passará a ser de R$ {aum:.2f}.')
