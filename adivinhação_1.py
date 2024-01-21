import random

def jogar():

    print("**********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000


    print("Escolha o nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("Defina o Nível:"))

    if (nivel == 1):
        total_de_tentativas = 15
    else:
        if (nivel == 2):
            total_de_tentativas = 8
        else:
            if (nivel == 3):
                total_de_tentativas = 3


    rodada = 1

    for rodada in range(1,  total_de_tentativas + 1 ):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        pontos_perdidos = abs(numero_secreto - chute)


        if (chute < 1 or chute > 100):
            print("Número inválido, tente novamente!")
            continue #irá continuar o código



        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break #irá parar o código
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")


            abs(pontos_perdidos)
            pontos = pontos - pontos_perdidos


    print("Fim do jogo")

