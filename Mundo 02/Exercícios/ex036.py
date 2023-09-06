"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela
não pode exceder 30% do salário ou então o empréstimo será negado."""

casa = float(input('Qual o valor da casa?: R$ '))
salario = float(input('Qual o salário do comprador?: R$ '))
tempo = int(input('Em quantos anos será efetuado o pagamento total?: '))

mensalidade = casa / (tempo * 12)
porcentagem_salario = salario * 30 / 100

if mensalidade <= porcentagem_salario:
    print(f'O valor total da casa é de R$ {casa:.2f}\n'
          f'O salário do comprador é de R$ {salario:.2f}\n'
          f'O prazo escolhido para pagamento total foi de {tempo:.0f} ano(s) ({tempo * 12:.0f} mes(es))\n'
          f'A parcela ficou no valor de R$ {mensalidade:.2f}\n'
          f'E equivale a menos de 30% do salário do comprador\n'
          f'Portanto, o empréstimo foi APROVADO!')
else:
    print(f'O valor total da casa é de R$ {casa:.2f}\n'
          f'O salário do comprador é de R$ {salario:.2f}\n'
          f'O prazo escolhido para pagamento total foi de {tempo:.0f} ano(s) ({tempo * 12:.0f} mes(es))\n'
          f'A parcela ficou no valor de R$ {mensalidade:.2f}\n'
          f'E equivale a mais de 30% do salário do comprador\n'
          f'Portanto, o empréstimo foi NEGADO!')
