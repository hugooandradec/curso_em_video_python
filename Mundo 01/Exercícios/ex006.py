"""Crie um algoritmo que leia um número e mostre seu dobro, triplo e a raiz quadrada"""

num = int(input('Digite um número: '))
dob = num * 2
tri = num * 3
rq = num ** (1/2)

print(f'Você digitou {num}.\n'
      f'O dobro de {num} é {dob}.\n'
      f'O triplo de {num} é {tri}.\n'
      f'A raiz quadrada de {num} é {rq:.2f}.')
