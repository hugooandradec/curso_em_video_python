"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor '999', que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)."""

contador = soma = 0
número = int(input('Digite um número inteiro qualquer [999 encerra o programa]: '))

while número != 999:
    contador += 1
    soma += número
    número = int(input('Digite um número inteiro qualquer [999 encerra o programa]: '))
print(f'\nForam digitados {contador} números e a soma entre eles é de {soma}!')
