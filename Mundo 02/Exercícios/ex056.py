"""Desenvolva um programa que leie o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo; Qual o nome do homem mais velho; Quantas mulheres tem menos de 20 anos."""

somaidade = 0
medidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    nome = str(input(f'Nome da {p}ª pessoa: ')).strip()
    idade = int(input(f'Idade da {p}ª pessoa: '))
    sexo = str(input(f'Sexo da {p}ª pessoa [M/F]: '))
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Fm' and idade < 20:
        totmulher20 += 1

medidade = somaidade / 4

print(f'\nA média de idade do grupo é de {medidade:.2f} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'{totmulher20} mulheres tem menos de 20 anos.')
