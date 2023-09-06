"""Faça um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0.50 por km
para viagens até 200km e R$ 0.45 para viagens mais longas."""

dist = float(input('Qual a distância da viagem?: '))

print(f'A distância da viagem será de {dist}km.')

if dist <= 200:
    print(f'Com um total de {dist}km, sua passagem ficará no valor de R$ {dist * 0.50:.2f}')
else:
    print(f'Com um total de {dist} km, sua passagem ficará no valor de R$ {dist * 0.45:.2f}')
