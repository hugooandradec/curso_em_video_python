"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido, quando o número solicitado for negativo."""

cont = 0
while True:
    num = int(input('Digite um número para ver sua tabuada [digite um número negativo para encerrar]: '))
    if num < 0:
        break
    cont += 1
    for cont in range(1, 11):
        print(f'{cont} X {num} = {cont * num}')
print('FIM')
