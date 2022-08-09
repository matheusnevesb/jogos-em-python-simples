# recebe um numero e fala se acima ou abaixo para o usuario ate adivinhar
# menu com 3 dificuldades
# sistema de pontuação
# Quando acabar perguntar se quer jogar de novo
import random

def jogar():
    pontuacao = 0
    jogo = True


    while (jogo == True):
        print("***************************************************************")
        print("Bem vindo ao jogo Numero Secreto!")
        print("***************************************************************")
        print("numero possivel de 1 a 1000")

        print("Facil: 20 tentativas F")
        print("Normal: 15 tentativas M")
        print("Dificil: 10 tentativas D")
        tentativa = input("escolha a dificuldade:")

        if (tentativa == 'f') or (tentativa == 'F'):
            chutes = 20
        elif (tentativa == 'm') or (tentativa == 'M'):
            chutes = 15
        elif (tentativa == 'd') or (tentativa == 'D'):
            chutes = 10

        numero = int(input("digite um numero: "))

        segredo = random.randint(1,1000)

        i = 1
        while (i < chutes) and (numero != segredo):
            if (numero > segredo):
                print("***************************************************************")
                print("chute acima do segredo")
                print("voce tem mais ", chutes - i, "tentativas")
                numero = int(input("digite um numero: "))

            elif (numero < segredo):
                print("***************************************************************")
                print("chute abaixo do segredo")
                print("voce tem mais ", chutes - i, "tentativas")
                numero = int(input("digite um numero: "))
            i +=1

        if numero == segredo:
            print("***************************************************************")
            print("Acertou!\nO numero secreto é igual a", segredo)
            print("Foi utilizado ", i , "tentativas")
            print("***************************************************************")

            if chutes == 20:
                pontuacao = pontuacao + (chutes - i)
        
            elif (chutes == 15):
                pontuacao = pontuacao + (chutes - i) * 3

            elif (chutes == 10 ):
                pontuacao = pontuacao + (chutes - i) * 5
            
            condicao = input("Gostaria de continuar? (sim ou nao)")

        else:
            print("***************************************************************")
            print("Acabou suas chances!")
            print("Numero secreto era: ", segredo, "!")
            print("Sua pontuação foi de: ", pontuacao, "pontos !")
            print("***************************************************************")
            pontuacao = 0

            condicao = input("Gostaria de jogar continuar? (sim ou nao)")

        if condicao == 'sim':
            jogo = True
        else:
            jogo = False
            

    if jogo == False:
        print("Obrigado por jogar!")
        print("Sua pontuação foi de: ", pontuacao, "pontos !")

if (__name__ == "__main__"):
    jogar()