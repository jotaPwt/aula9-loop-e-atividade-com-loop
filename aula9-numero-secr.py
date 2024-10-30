import random

chance = range(1, 4)

for i in chance:
    chute = int(input('Digite um numero'))
    aleatorio = random.randint(1,6)
    if chute == aleatorio:
        print('Você acertou em cheio')
        break
    else:
        print(f'Voce errou, {i} chances restantes')