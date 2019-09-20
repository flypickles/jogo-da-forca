import random

def abertura():
    print("\n***** !BEM VINDO AO JOGO DA FORCA DO LUANZINHO! *****\n")
    print("\n*****   !APENAS POKEMONS DA PRIMEIRA GERAÇÃO!   *****\n")


def palavraSecreta():
    palavras = []
    arq = open('D:/GitHub/jogo-da-forca/Jogo da Forca/palavras.txt', 'r')
    # definir o caminho padrão, não esquece

    for linhas in arq:
        linhas = linhas.rstrip()
        palavras.append(linhas)
    arq.close()

    palavra_random = random.choice(palavras)

    return palavra_random

def inicializaPalavraSecreta():
    palavras_acertadas = []

    for i in range(len(palavraSecreta())):
        palavras_acertadas.append("_")

    return palavras_acertadas

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

enforcou = False
acertou = False
erros = 0

#nada da certo foda-se