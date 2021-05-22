# Programa onde 4 jogadores jogam um dado e tenham resultados aleatorios. 
# Informar o Ganhador, aquele que tirou o maior numero.


print(" ==>>> Projeto simulador de dados <<<== ")
from random import randint
from time import sleep
from operator import itemgetter
from warnings import simplefilter

# Guardar o resultado em um dicionario
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6),}
ranking = list()

# Colocar o dicionario em ordem
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Informar o vencedor que é aquele que tirou o maior numero no dado.
print('-----'*20)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]};')
    sleep(1)



