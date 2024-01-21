import random

def jogar():

    imprime_abertura()
    palavra_secreta = carry_sword()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)


    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    #Enquanto nao enforcou e nao acertou printar jogando
    while not enforcou and not acertou:

        chute = input("Tente uma letra:")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:

            tentativas += 1
        print(letras_acertadas)

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas

        print("Você cometeu {} de 6 erros".format(tentativas))

    if acertou:
        imprime_vitoria()
    else:
        imprime_derrota(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

    print("Fim do jogo")



    if (__name__=="___main___"):
        jogar()

def imprime_abertura():
    print("**********************************")
    print("Bem vindo ao jogo de forca!")
    print("**********************************")

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def carry_sword():
    arquivo = open("palavra.txt", "r")
    palavra = []


    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavra))
    palavra_secreta = palavra[numero].upper()

    # tambem pode ser feito como:
    # for letra in palavra_secreta:
    # letras_acertadas.append("_")
    return palavra_secreta
