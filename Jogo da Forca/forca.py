import random
import pygame

pygame.mixer.init()

pygame.mixer.music.load('battle.mp3')
pygame.mixer.music.play()

erros = 0
letras_acertadas = []
letras_erradas = []

def abertura():
    print("\n*****        BEM VINDO AO JOGO DA FORCA!       *****")
    print("\n*****   APENAS POKEMONS DA PRIMEIRA GERAÇÃO!   *****")

def palavraSecreta():
    palavras = []
    arq = open('C:\Temp\Trabalho Python\Jogo da Forca\palavras.txt', 'r')
    #definir um caminho que funcione em qualquer lugar 

    for linhas in arq: #adiciona a lista de palavras para um array
        linhas = linhas.rstrip()
        palavras.append(linhas)
    arq.close()

    global palavra_random
    palavra_random = list(random.choice(palavras)) #pega uma palavra aleatória do array e transforma em lista

def palavraOculta():
    global letras_ocultas 
    letras_ocultas = []
    
    for i in range(len(palavra_random)): #transforma a palavra aleatoria em "_" para ficar oculta
        letras_ocultas.append("_")
    
def pedeChute():
    global letra
    letra = input("Chute uma letra: ").upper().strip() #pede uma letra e já transforma ela em maiúscula e retirar qualquer espaço que houver
    
def marcaChute(): #vai conferir em qual posição da palavra se encontra a letra e substituir em "letras_ocultas"
    for x in range (len(palavra_random)):
        if letra == palavra_random[x]:
            letras_ocultas[x] = letra
    print()
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
    desenho(erros)
    print(letras_ocultas)
    print("Letras acertadas: {}" .format(letras_acertadas))
    print("Letras erradas: {}" .format(letras_erradas))
    print()
    pedeChute()

    if (len(letra) != 1):
        print("\nDigite apenas UMA letra")
    elif (letra in letras_acertadas or letra in letras_erradas):
        print("\nVocê já tentou essa letra")
    
    if (letra in palavra_random):
        marcaChute()
        if (letra not in letras_acertadas):
            letras_acertadas.append(letra)
        
    if (letra not in palavra_random and letra not in letras_erradas and len(letra) == 1):
        erros += 1
        letras_erradas.append(letra)

    if (letras_ocultas == palavra_random):
        print("Acertou!")
        print("A palavra secreta era: {}" .format(palavra_random))
        acertou = True
    elif (erros == 6):
        enforcou = True
        desenho(6)
        print("Você perdeu!")
        print("A palavra secreta era: {}" .format(palavra_random))
