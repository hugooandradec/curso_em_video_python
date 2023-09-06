"""cont = 1
while True:
    print(f'{cont} - ', end='')
    cont += 1
    if cont == 51:
        break
print('FIM')"""

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

