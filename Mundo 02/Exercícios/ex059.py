"""Crie um programa que leia dois valores e mostre um menu na tela:
[1] - Somar
[2] - Multiplicar
[3] - Maior número
[4] - Digitar novos números
[5] - Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep

op = 0
maior = 0

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

while op != 5:
    print('\nEscolha uma das opções abaixo: \n'
          '[1] - Somar\n'
          '[2] - Multiplicar\n'
          '[3] - Maior número\n'
          '[4] - Digitar novos números\n'
          '[5] - Sair do programa\n')

    op = int(input('Qual opção você escolhe?: '))

    if op == 1:
        resultado = num1 + num2
        print(f'\nA soma entre {num1:.2f} e {num2:.2f} é de {resultado:.2f}.')
        sleep(3)
    elif op == 2:
        resultado = num1 * num2
        print(f'\nA multiplicação entre {num1:.2f} e {num2:.2f} é de {resultado:.2f}')
        sleep(3)
    elif op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'\nO maior valor digitado é {maior:.2f}')
        sleep(3)
    elif op == 4:
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
    elif op == 5:
        print('\nSaindo do programa...')
        sleep(3)
    else:
        print('\nOpção inválida. Tente novamente.')
        sleep(3)
