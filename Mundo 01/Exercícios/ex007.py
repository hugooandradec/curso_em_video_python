"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2

print(f'A primeira nota foi {n1:.2f} e a segunda foi {n2:.2f}.\n'
      f'A média do aluno foi de {med:.2f}.')
