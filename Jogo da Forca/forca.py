import random
#Funções
def abertura():
    print("\n***** !BEM VINDO AO JOGO DA FORCA DO LUANZINHO! *****\n")
    print("\n*****   !APENAS POKEMONS DA PRIMEIRA GERAÇÃO!   *****\n")
    
def palavra_secreta():
    global palavras
    palavras = []
    palavras_acertadas = []
    arq = open('C:/Temp/Trabalho Python/Jogo da Forca/palavras.txt', 'r')

    for linhas in arq:
        linhas = linhas.rstrip()
        palavras.append(linhas)
    arq.close()
    
    palavraRandom = random.choice(palavras)

    for i in range(len(palavraRandom)):
        palavras_acertadas.append("_")
    
    print(palavras_acertadas)
     
def pede_chute():
    chute = input("Chute uma letra: ")
    

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

palavra_secreta()
