"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais."""

palavras = ('PERA', 'UVA', 'MAÇA', 'MAMAO', 'BANANA', 'ABACAXI', 'ABACATE', 'GOIABA', 'KIWI', 'MANGA')
vogais = 'AEIOU'

print()
for palavra in palavras:
    print(f'Na palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
    print()
