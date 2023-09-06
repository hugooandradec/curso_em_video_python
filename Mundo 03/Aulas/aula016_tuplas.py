lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Vou comer pra caramba!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.index(5))

pessoa = ('Gustavo', 39, 'M', 99.88)
del pessoa
print(pessoa)
