"""Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos, usando a
estrutura while."""

primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))

cont = 1
termo = primeiro

while cont <= 10:
    print(f'O {cont}º termo da PA é: {termo}')
    termo += razão
    cont += 1
