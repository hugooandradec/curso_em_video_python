"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor"""

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1

print(f'Você digitou {num}.\n'
      f'O antecessor de {num} é {ant}.\n'
      f'O sucessor de {num} é {suc}.')
