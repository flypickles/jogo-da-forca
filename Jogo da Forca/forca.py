import random

def abertura():
    print("\n*****   !BEM VINDO AO JOGO DA FORCA!            *****\n")
    print("\n*****   !APENAS POKEMONS DA PRIMEIRA GERAÇÃO!   *****\n")

def palavraSecreta():
    palavras = []
    arq = open('C:/Temp/Trabalho Python/Jogo da Forca/palavras.txt', 'r')
    # Como definir o caminho certo?

    for linhas in arq:
        linhas = linhas.rstrip()
        palavras.append(linhas)
    arq.close()

    palavra_random = random.choice(palavras)

    return palavra_random

def palavraOculta():
    letras_ocultas = []

    for i in range(len(palavraSecreta())):
        letras_ocultas.append("_")

    return letras_ocultas

def pedeChute(chute):
    chute = input("Chute uma letra: ")
    if len(chute) != 1:
        print("Chute apenas UMA letra!")
    return chute

def desenho(erros):
    if erros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|    |\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif erros == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|    | ")
        print("|     \ ")
        print("_      ")
        print()
    elif erros == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print("_      ")
        print()


acertou = False
enforcou = False
chute = ""

while acertou == False and enforcou == False:
    print(pedeChute(chute))
    
    for i in range(len(palavraSecreta())):
        if chute in palavraSecreta()[i]:
            palavraOculta()[i] = chute
    
#error  


          
