from random import randrange

def abertura():
    print("\n***** !BEM VINDO AO JOGO DA FORCA DO LUANZINHO! *****\n")
    print("\n***** !APENAS POKEMONS DA PRIMEIRA GERAÇÃO! *****\n")

def palavra_secreta():
    palavras = ["T", "E", "S", "T", "E"]
    letras_acertadas = []
    letras_acertadas.append("-")

    for i in range(0, len(palavras)):  
        print(palavras[i])

abertura()        
palavra_secreta()

