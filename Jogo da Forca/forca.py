import random
import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("battle.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.4)

def abertura():
    print("\n*****        BEM VINDO AO JOGO DA FORCA         *****")
    print("\n*****    APENAS POKEMONS DA PRIMEIRA GERAÇÃO!   *****")

#palavraSecreta() Vai ler o arquivo palavras.txt, jogar as palavras para um array, pegar uma palavra aleatória do array e transformar em lista   
def palavraSecreta():
    palavras = []
    arq = open('palavras.txt', 'r')

    for linhas in arq: 
        linhas = linhas.rstrip()
        palavras.append(linhas)
    arq.close()

    global palavra_random
    palavra_random = list(random.choice(palavras)) 

#palavraOculta() Vai receber a palavra aleatória, ver quantos caracteres ela tem e adicionar "_" no lugar
def palavraOculta():
    global letras_ocultas 
    letras_ocultas = []
    
    for i in range(len(palavra_random)): 
        letras_ocultas.append("_")

#pedeChute() Pede uma letra e já transforma ela em maiúscula e retirar qualquer espaço que houver    
def pedeChute():
    global letra
    letra = input("Chute uma letra: ").upper().strip()
    
#marcaChute() vai conferir em qual posição da palavra se encontra a letra e substituir em "letras_ocultas"    
def marcaChute(): 
    for x in range (len(palavra_random)):
        if letra == palavra_random[x]:
            letras_ocultas[x] = letra
    print()
    print()
#desenho() Monta o desenho da forca conforme o jogador erra o chute
def desenho(numErros): 
    if numErros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("__________")
        print()
    elif numErros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("__________")
        print()
    elif numErros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print("__________")
        print()
    elif numErros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|    |\ ")
        print("|    | ")
        print("|      ")
        print("__________")
        print()
    elif numErros == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|    | ")
        print("|      ")
        print("__________")
        print()
    elif numErros == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|    | ")
        print("|     \ ")
        print("__________")
        print()
    elif numErros == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0   'p-pikachu...' ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print("__________")
        print()

erros = 0
letras_acertadas = []
letras_erradas = []

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

        pygame.mixer.pause()
        pygame.mixer.music.load("victory.mp3")
        pygame.mixer.music.play()
        pygame.event.wait()
        
        
    elif (erros == 6):
        enforcou = True
        desenho(6)
        print("Você perdeu!")
        print("A palavra secreta era: {}" .format(palavra_random))
        
        pygame.mixer.pause()
        pygame.mixer.music.load("defeat.mp3")
        pygame.mixer.music.play()
        pygame.event.wait()
