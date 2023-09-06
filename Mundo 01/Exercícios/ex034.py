"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$ 1.200,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

sal = float(input('Qual o salário do funcionário?: R$ '))

if sal > 1200:
    print(f'O salário do funcionário é de R$ {sal:.2f}\n'
          f'Com o aumento de 10%, ele passará a receber R$ {sal + sal * 10 / 100:.2f}')
else:
    print(f'O salário do funcionário é de R$ {sal:.2f}\n'
          f'Com o aumento de 15%, ele passará a receber R$ {sal + sal * 15 / 100:.2f}')
