"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$ 7.00 por cada km acima do limite."""

vel = int(input('Qual a velocidade, em km, que o carro passou no radar?: '))

print(f'O carro passou à {vel} km/h.')

if vel > 80:
    vel_acima = vel - 80
    print('O carro passou acima do limite permitido que é de 80km/h e foi multado.\n'
          'O valor da multa é de R$ 7.00 por cada km acima do limite.\n'
          f'O carro passou {vel_acima}km/h acima do limite.\n'
          f'O valor da multa é de R$ {vel_acima * 7.00:.2f}')
else:
    print('O carro passou dentro da velocidade permitida.')
