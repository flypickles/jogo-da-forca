import random
global erros

def abertura():
    print("\n*****        !BEM VINDO AO JOGO DA FORCA!       *****\n")
    print("\n*****   !APENAS POKEMONS DA PRIMEIRA GERAÇÃO!   *****\n")
   #print("\n*****              Luan C. Nunes                *****\n")

def palavraSecreta():
    palavras = []
    arq = open('C:\Temp\Trabalho Python\Jogo da Forca\palavras.txt', 'r') 

    for linhas in arq: #adiciona a lista de palavras para um array
        linhas = linhas.rstrip()
        palavras.append(linhas)
    arq.close()

    global palavra_random

    palavra_random = list(random.choice(palavras)) #pega uma palavra aleatória do array e transforma em lista

    print(palavra_random)

def palavraOculta():

    global letras_ocultas 
    letras_ocultas = []
    
    for i in range(len(palavra_random)): #transforma a palavra aleatoria em "_" para ficar oculta
        letras_ocultas.append("_")
    
    print(letras_ocultas)

def pedeChute():
    global letra
    letra = input("Chute uma letra: ").upper().strip()  
    
def confereChute(): #Vai conferir se a letra chutada existe na palavra secreta e substituir o "_" pela letra
    if letra in palavra_random:
        for x in range (len(palavra_random)):
            if letra == palavra_random[x]:
                letras_ocultas[x] = letra
    else:
        print("Errou!")
        
    print()
    print(letras_ocultas)
    print()

def desenho(numErros): #conforme os chutes errados aumentam, a forca vai se montando
    if numErros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif numErros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif numErros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif numErros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|    |\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif numErros == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
    elif numErros == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|    | ")
        print("|     \ ")
        print("_      ")
        print()
    elif numErros == 6:
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

abertura()
palavraSecreta()
palavraOculta()
print()

while acertou == False and enforcou == False:
    pedeChute()
    confereChute()
    
    if letras_ocultas == palavra_random:
        print("Acertou!")
        acertou = True
    #elif erros == 6:
        #print("Você perdeu!")
        #print("A palavra secreta era: {}" .format(palavra_random))
        #enforcou = True