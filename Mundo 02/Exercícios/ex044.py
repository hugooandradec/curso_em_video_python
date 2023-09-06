"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:

- À vista em dinheiro: 10% de desconto
- À vista no cartão: 5% de desconto
- 2x: Preço normal
- 3x ou mais: 20% de juros"""

valor = float(input('Qual o valor do produto?: R$'))

print('\nQual a forma de pagamento?\n'
      '[1] - Dinheiro (10% de desconto)\n'
      '[2] - 1x no cartão (5% de desconto)\n'
      '[3] - 2x no cartão (sem juros)\n'
      '[4] - 3x ou mais (20% de juros)\n')
pg = int(input('Digite a opção escolhida: '))

if pg == 1:
    print('\nA forma de pagamento escolhida foi Dinheiro\n'
          f'O valor da compra é de R${valor:.2f}\n'
          f'Com o desconto de 10%, ficou no valor de R${valor - (valor * 10 / 100):.2f}')
elif pg == 2:
    print('\nA forma de pagamento escolhida foi 1x no cartão\n'
          f'O valor da compra é de R${valor:.2f}\n'
          f'Com o desconto de 5%, ficou no valor de R${valor - (valor * 5 / 100):.2f}')
elif pg == 3:
    print('\nA forma de pagamento escolhida foi 2x no cartão\n'
          f'O valor da compra é de R${valor:.2f}\n'
          f'Que será paga em 2x de R${valor / 2:.2f}')
elif pg == 4:
    novoValor = (valor + (valor * 20 / 100))
    parcela = int(input('Em quantas vezes será paga a compra? (máx. 10x): '))
    print('\nA forma de pagamento escolhida foi 3x ou mais\n'
          f'O valor da compra é de R${valor:.2f}\n'
          f'Com o acréscimo de 20%, ficou no valor de R${novoValor:.2f}\n'
          f'\nA compra de R${novoValor:.2f} será paga em {parcela}x\n'
          f'Ficando então {parcela}x de R${novoValor / parcela:.2f}')
else:
    print('\nVocê digitou uma opção inválida. Reinicie a aplicação!')
