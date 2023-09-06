"""Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado"""

dias = int(input('Por quantos dias o carro ficou alugado?: '))
km = float(input('Quantos KMs rodados?: '))

diaspg = dias * 60
kmpg = km * 0.15

print(f'O carro ficou alugado por {dias} dias;\n'
      f'O total de KMs rodados foi de {km:.2f}KMs;\n'
      f'O valor a ser pago pelos dias é de R$ {diaspg:.2f};\n'
      f'O valor a ser pago pelos KMs é de R$ {kmpg:.2f};\n'
      f'O valor final a ser pago é de R$ {diaspg + kmpg:.2f}!')
