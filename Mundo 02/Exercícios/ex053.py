"""Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderandos os espaços."""

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
inverso = frase[::-1]

print(f'A frase digitada foi: {frase}\n'
      f'A frase digitada, ao contrário é: {inverso}')
if frase == inverso:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
