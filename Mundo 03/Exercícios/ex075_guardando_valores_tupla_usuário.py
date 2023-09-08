"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
A - Quantas vezes o valor 9 apareceu.
B - Em que posição foi digitado o primeiro valor 3
C - Quais foram os números pares."""


núm = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores {núm}')

print(f'O valor 9 apareceu {núm.count(9)} vezes')

if 3 in núm:
    print(f'O valor 3 apareceu pela primeira vez na posição {núm.index(3) + 1}ª')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print(f'Os valores pares digitados foram: ', end='')

for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print('0', end='')
