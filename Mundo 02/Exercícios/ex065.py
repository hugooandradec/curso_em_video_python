"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores, qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores."""

resposta = 'S'
soma = quantidade = média = maior = menor = 0
while resposta in 'Ss':
    número = int(input('Digite um número: '))
    soma += número
    quantidade += 1
    if quantidade == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
média = soma / quantidade
print(f'Você digitou {quantidade} números e a média foi {média:.2f}.\n'
      f'O maior número foi {maior:.0f} e o menor foi {menor:.0f}.')
