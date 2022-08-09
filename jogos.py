import forca
import Numero_Secreto

def escolhe_jogo():
    print("***************************************************************")
    print("bem vindo,Escolha o seu jogo!")
    print("***************************************************************")

    print("(1) Forca")
    print("(2) Numero Secreto")

    jogo = int(input("Digite o numero do jogo desejado: "))

    if (jogo == 1):
        forca.jogar()

    elif (jogo == 2):
        Numero_Secreto.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()