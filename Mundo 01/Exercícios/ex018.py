"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo"""

from math import cos, sin, tan, radians

ang = float(input('Digite o valor do ângulo: '))
ang_rads = radians(ang)
cos_ang = cos(ang_rads)
sin_ang = sin(ang_rads)
tan_ang = tan(ang_rads)

print(f'O ângulo digitado foi {ang}°\n'
      f'O valor do seno é de {sin_ang:.3f}\n'
      f'O valor do cosseno é de {cos_ang:.3f}\n'
      f'O valor da tangente é de {tan_ang:.3f}')
