"""Escreva um programa que converta uma temperatura digitada em °C e converta para °F."""

tempC = float(input('Qual a temperatura em °C que você quer converter para °F? '))
tempF = tempC * 1.8 + 32

print(f'A temperatura de {tempC:.2f}°C equivale a {tempF:.2f}°F')
