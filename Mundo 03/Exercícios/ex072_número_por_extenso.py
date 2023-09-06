"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)e mostrá-lo por extenso."""

número_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    número_usuário = int(input('Digite um número entre 0 e 20: '))
    if 0 <= número_usuário <= 20:
        print(f'O número digitado foi {número_usuário} ({número_extenso[número_usuário]})')
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Deseja continuar?[S/N]: ')).upper().strip()
        if resposta == 'N':
            print('FIM DO PROGRAMA!')
            break

    else:
        print('Tente novamente. ', end='')
