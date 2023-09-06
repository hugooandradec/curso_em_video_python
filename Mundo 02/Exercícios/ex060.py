"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5*4*3*2*1 = 120"""

n = int(input('Digite um número: '))
c = n
f = 1

print(f'Calculando {n}!', end=': ')
while c > 0:
    print(f'{c}', end=' ')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f'{f}')
