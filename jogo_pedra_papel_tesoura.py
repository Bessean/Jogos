# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep      


itens = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)
print(''' Escolha uma opção:  
[0] PEDRA
[1] PAPEL 
[2] TESOURA ''')
voce = int(input('Qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('>>>> O computador escolheu {} <<<<'.format(itens[computer]))
print('>>>> Você escolheu {} <<<<'.format(itens[voce]))

if computer == 0:
    if voce == 0:
        print('Empatados!')
    elif voce == 1:
        print('Você Ganhou!')
    elif voce == 2:
        print('Computador ganhou!')
    else:
        print('Opção inválida!')            

elif computer == 1: 
    if voce == 1:
        print('Empatados!')
    elif voce == 0:
        print('Computador ganhou!')
    elif voce == 2:
        print('Você ganhou!')
    else:
        print('Opção inválida!')   

elif computer == 2: #tesoura
    if voce == 2:
        print('Empatados!')
    elif voce == 0:#pedra
        print('Você ganhou!')
    elif voce == 1:##papel
        print('Computador ganhou!')
    else:
        print('Opção inválida!')   