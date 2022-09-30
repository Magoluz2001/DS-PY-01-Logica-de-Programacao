import random
from arquivo_palavras import lista_palavras

chances = 5
chutes = []
condicao = False
forca = str(lista_palavras[random.randrange(len(lista_palavras))])

while not(condicao):
    for letra in forca:
        if (letra.lower() in chutes):
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("")
    condicao = True

    chute = input(f"Você tem {chances} chances. Tente um letra: ")
    chutes.append(chute.lower())
    if (chute.lower() not in forca.lower()):
        chances -= 1
        if chances == 0:
            break

    condicao = True
    for chute in forca:
        if (chute.lower() not in chutes):
            condicao = False

if condicao == False:
    print("Você descobriu a palavra.")
else:
    print("Suas chances acabaram. Fim de jogo.")


