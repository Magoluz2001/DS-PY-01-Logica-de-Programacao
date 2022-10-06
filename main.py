import random
from arquivo_palavras import lista_palavras

chances = 5
chutes = []
condicao = False

# Pega uma palavra aleatória da lista
forca = str(lista_palavras[random.randrange(len(lista_palavras))])

while not(condicao):

    # Exibe as letras que já foram inseridas corretamento pelo usuário e exibe _ para letras da palavra que não foram inseridas
    for letra in forca:
        if (letra.lower() in chutes):
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("")
    condicao = True

    chute = input(f"Você tem {chances} chances. Tente um letra: ") # Recebe o input do usuário
    chutes.append(chute.lower()) # Adiciona o input a lista de inputs

    # Caso não exista na palavra escolhida
    if (chute.lower() not in forca.lower()):
        chances -= 1 # Decrementa a variável de chances
        if chances == 0: # Quando as chances chegam a 0 o loop para
            break

    condicao = True

    # Caso alguma letra da palavra não esteja nos chutes o loop continua
    for chute in forca:
        if (chute.lower() not in chutes):
            condicao = False

# Essa condicional é ativada ao final do jogo, seja vitória ou derrta.
if condicao == False:
    print("Você descobriu a palavra.")
else:
    print("Suas chances acabaram. Fim de jogo.")


