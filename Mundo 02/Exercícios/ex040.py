"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida:

- Média abaixo de 5.00: Reprovado
- Média entre 5.00 e 6.90: Recuperação
- Média 7.00 ou acima: Aprovado"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

med = (n1 + n2) / 2

print(f'Você tirou {n1:.2f} e {n2:.2f} e sua média foi de {med:.2f}!')
if med < 5.00:
    print('Você está reprovado.')
elif 5.00 <= med <= 6.99:
    print('Você está de recuperação.')
else:
    print('Você está aprovado')
