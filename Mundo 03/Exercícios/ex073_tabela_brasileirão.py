"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Brasileirão, na ordem de colocação.
Depois mostre:
A - Apenas os 5 primeiros colocados.
B - Os últimos 4 colocados da tabela.
C - Uma lista com os times em ordem alfabética.
D - Em que posição na tabela está o Flamengo."""

tupla_times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Atlético-PR', 'Fortaleza',
               'Atlético-MG', 'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia',
               'Santos', 'Vasco', 'América-MG', 'Coritiba')

print('\nOs cinco primeiros colocados são: ')
for posiçao, time in enumerate(tupla_times[:5]):
    print(f'{posiçao + 1}º - {time}')

print('\nOs quatro últimos colocados são: ')
for posiçao in range(17, 21):
    time = tupla_times[posiçao - 1]
    print(f'{posiçao}º - {time}')

tupla_ordenada = sorted(tupla_times)
print('\nEsses são os times em ordem alfabética: ')
for contador in range(0, len(tupla_ordenada)):
    print(f'{tupla_ordenada[contador]}')


print(f'\nO Flamengo está na {tupla_times.index("Flamengo") + 1}ª posição!')
