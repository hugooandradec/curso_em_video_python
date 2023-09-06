"""Desenvolva um programa que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
com a tabela abaixo:

- Abaixo de 18.50: Abaixo do peso
- Entre 18.50 e 25.00: Peso ideal
- 25.00 até 30.00: Sobrepeso
- 30.00 até 40.00: Obesidade
- Acima de 40:00: Obesidade mórbida"""

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

print(f'Você tem {peso:.2f}kg, {altura:.2f}m e seu IMC é de {imc:.2f}.')

if imc < 18.50:
    print('Você está abaixo do peso!')
elif imc < 25.00:
    print('Você esta no peso ideal!')
elif imc < 30.00:
    print('Você está com sobrepeso!')
elif imc < 40.00:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')
