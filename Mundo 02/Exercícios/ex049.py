"""Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for"""

num = int(input('Digite um número: '))

print(f'\nSegue abaixo a tabúada de multiplicação do número {num}.\n')

for c in range(1, 11):
    print(f'{num} x {c} = {c * num}')
