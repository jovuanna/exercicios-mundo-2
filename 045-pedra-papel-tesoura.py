from random import randint
from time import sleep #espera um tempo pra printar
print('''PEDRA, PAPEL E TESOURA

[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
computador = randint(0, 2) #o comuputador sorteia um número inteiro entre 0 e 2
opcoes = int(input("Escolha uma das opções: "))

print("-"*20)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!")
sleep(0.5)

if opcoes == 0:
    print("-" * 20)
    print("Jogador jogou Pedra.")
    if computador == 0:
        print("Computador jogou Pedra.")
        print("-" * 20)
        print("JOGADA EMPATADA")
    elif computador == 1:
        print("Computador jogou Papel.")
        print("-" * 20)
        print("JOGADOR VENCE")
    else:
        print("Computador jogou Tesoura.")
        print("-" * 20)
        print("COMPUTADOR VENCE")
elif opcoes == 1:
    print("-" * 20)
    print("Jogador jogou Papel.")
    if computador == 0:
        print("Computador jogou Pedra.")
        print("-" * 20)
        print("JOGADOR VENCE")
    elif computador == 1:
        print("Computador jogou Papel.")
        print("-" * 20)
        print("JOGADA EMPATADA")
    else:
        print("Computador jogou Tesoura.")
        print("-" * 20)
        print("COMPUTADOR VENCE")
elif opcoes == 2:
    print("-" * 20)
    print("Jogador jogou Tesoura.")
    if computador == 0:
        print("Computador jogou Pedra.")
        print("-" * 20)
        print("COMPUTADOR VENCE")
    elif computador == 1:
        print("Computador jogou Papel.")
        print("-" * 20)
        print("JOGADOR VENCE")
    else:
        print("Computador jogou Tesoura.")
        print("-" * 20)
        print("JOGADA EMPATADA")
else:
    print("Escolha uma opção válida.")
