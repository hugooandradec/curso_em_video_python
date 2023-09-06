"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:

1 - para binário
2 - para octal
3 - para hexadecimal"""

bases = ('Binário', 'Octal', 'Hexadecimal')

num = int(input('Digite um número para ser feita a conversão: '))

print('Escolha uma das opções abaixo, digitando o número correspondente\n'
      '1 - Binário\n'
      '2 - Octal\n'
      '3 - Hexadecimal\n')
escolha = int(input('Qual base de conversão você quer utilizar?: '))

if escolha == 1:
    print(f'O número {num} convertido na base {bases[escolha - 1]} equivale a: {bin(num)[2:]}')
elif escolha == 2:
    print(f'O número {num} convertido na base {bases[escolha - 1]} equivale a: {oct(num)[2:]}')
elif escolha == 3:
    print(f'O número {num} convertido na base {bases[escolha - 1]} equivale a: {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente!')
