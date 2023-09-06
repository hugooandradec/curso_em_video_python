"""A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Júnior
- Até 25 anos: Sênior
- Acima: Master"""

from datetime import date

ano_nascimento = int(input('Qual o ano de nascimento do atleta?: '))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é a mirim!')
elif idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é a infantil!')
elif idade <= 19:
    print(f'Você tem {idade} anos e sua categoria é a júnior!')
elif idade <= 25:
    print(f'Você tem {idade} anos e sua categoria é a sênior!')
else:
    print(f'Você tem {idade} anos e sua categoria é a master!')
