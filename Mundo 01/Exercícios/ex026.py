"""Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez
Em que posição ela aparece pela última vez"""

frase = str(input('Digite uma frase qualquer: ')).strip().lower()

print(f'A quantidade de letras "A" na frase é de: {frase.count("a")}\n'
      f'A letra "A" aparece pela primeira vez na posição: {frase.find("a") + 1} \n'
      f'A letra "A" aparece pela última vez na posição: {frase.rfind("a") + 1}')
