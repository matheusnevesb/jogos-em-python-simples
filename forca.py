import random

def jogar():
    
    imprime_mensagem_abertura()
    
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    # letras_acertadas = []

    # for letra in palavra_secreta:
    #     letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você acertou!!")

    else:
        print("Você perdeu!!")



def imprime_mensagem_abertura():
    print("***************************************************************")
    print("bem vindo ao Forca!")
    print("***************************************************************")

def carrega_palavra_secreta():
    arquivo = open("palavra.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):   
    return ["_" for letra in palavra]
    
    

if (__name__ == "__main__"):
    jogar()
    

