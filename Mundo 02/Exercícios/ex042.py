"""Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes"""

print('Digite 3 segmentos abaixo para verificarmos se eles podem formar um triângulo.\n'
      'Em seguida vamos verificar qual tipo de triângulo será formado!\n')

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
      if a == b == c:
            print(f'Os segmentos {a:.2f}, {b:.2f} e {c:.2f} podem formar um triângulo, sendo ele o: Equilátero.')
      elif a == b or b == c or c == a:
            print(f'Os segmentos {a:.2f}, {b:.2f} e {c:.2f} podem formar um triângulo, sendo ele o: Isósceles.')
      elif a != b != c:
            print(f'Os segmentos {a:.2f}, {b:.2f} e {c:.2f} podem formar um triângulo, sendo ele o: Escaleno.')
else:
      print(f'Os segmentos {a:.2f}, {b:.2f} e {c:.2f} não podem formar um triângulo.')
