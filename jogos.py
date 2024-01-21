
import forca 
import adivinhação_1

print("**********************************")
print("Escolha o seu jogo!")
print("**********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo:"))

if (jogo == 1):
    print("Jogando da forca")
    forca.jogar()

elif(jogo == 2 ):
    print("Jogando da adivinhação")
    adivinhação_1.jogar()


