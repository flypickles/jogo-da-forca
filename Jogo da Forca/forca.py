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

    palavra_random = list(random.choice(palavras))

    return palavra_random

def palavraOculta(passwd):
    letras_ocultas = []

    for i in range(len(passwd)):
        letras_ocultas.append("_")

    return letras_ocultas

# def pedeChute()
    

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
passwd = palavraSecreta()

print(passwd)
print(palavraOculta(passwd))                # Isso não da certo.

while acertou == False and enforcou == False:
    chute = input("Qual letra você chuta? ")

    for i in range(len(palavraSecreta())):
        if chute == passwd[i]:
            palavraOculta()[i] = chute
        palavraOculta()

#erro erro erro erro