"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer continuar . No final, mostre:
1 - quantas pessoas tem mais de 18 anos.
2 - quantos homens foram cadastrados.
3 - quantas mulheres tem menos de 20 anos."""

cont_idade = cont_homem = cont_mulher = cont_total = 0

print('CADASTRO DE PESSOAS\n')

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M]/[F]: ')).upper().strip()
    cont_total += 1
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja fazer um novo cadastro? [S]/[N]:').upper()).strip()
    if resp == 'N':
        break

print(f'\nTotal de pessoas cadastradas: {cont_total}\n'
      f'Total de pessoas com mais de 18 anos: {cont_idade}\n'
      f'Total de homens: {cont_homem}\n'
      f'Total de mulheres com menos de 20 anos: {cont_mulher}\n')

print('PROGRAMA ENCERRADO!')
