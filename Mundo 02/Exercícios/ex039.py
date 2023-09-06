"""Faça um programa que leia a data de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar e o tempo que falta
- Se é a hora de se alistar
- Se já passou do tempo do alistamento e quanto tempo passou"""

from datetime import date

ano = int(input('Qual o ano de nascimento?: '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    print(f'Você tem {idade} ano(s) e terá que se alistar daqui {18 - idade} ano(s), em {ano + 18}!')
elif idade == 18:
    print(f'Você tem {idade} ano(s) e é hora de se alistar!')
else:
    print(f'Você tem {idade} ano(s) e o momento para se alistar foi há {idade - 18} ano(s) atrás, em {ano + 18}!')
