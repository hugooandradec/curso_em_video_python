"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m²."""

larg = float(input('Qual a largura da parede?: '))
alt = float(input('Qual a altura da parede?: '))
area = larg * alt
tinta = 2

print(f'A largura da parede é de {larg:.2f} metros;\n'
      f'A altura da parede é de {alt:.2f} metros;\n'
      f'A área total é de {area:.2f}m²;\n'
      f'A quantidade necessária de tinta para pintar a parede será de {area / tinta:.2f} litros.')
