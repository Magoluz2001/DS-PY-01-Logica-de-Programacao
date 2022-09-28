import random
from arquivo_palavras import lista_palavras

# Dados internos
erros = 0
letras_restantes = 0
palavra_escolhida = []
condicao = True

# Dados externos
letra_usuario = str

#Seleciona a palavra e exibe o jogo no terminal para o usuário
palavra_escolhida = lista_palavras[random.randrange(len(lista_palavras))]
letras_restantes = len(palavra_escolhida)

print(f"""Bem vind@ ao jogo da forca!!

A sua palavra tem {len(palavra_escolhida)} letras""")

while (condicao):

    letra_usuario = input("Insira uma letra:")
    
    if not(letra_usuario in palavra_escolhida):

        erros += 1

        letra_usuario = input(f"""A letra {letra_usuario} não existe nessa palavra. Você ainda tem {erros} chances.
        
        Insira uma letra:""")
    
    else:
        
        letras_restantes -= 1

        palavra_usuario = input(f"""Você acertou uma letra. Continue até decifrar a palavra.
        
        Insira uma letra:""")



    



    


    


