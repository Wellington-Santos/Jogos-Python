import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 51)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil \n(2) Médio \n(3) Difícil")

    nivel = int(input("Escolha um nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #print(numero_secreto)

    for tentativa  in range(1, total_de_tentativas + 1):
    
        print("tentativa {} de {}".format(tentativa, total_de_tentativas))
        chute_str = input("Digite o seu numero entre 1 e 50: ")
        print("Você digitou ", chute_str)    
        chute = int(chute_str)

        if(chute < 1 or chute > 50):
            print("Você deve informar um número entre 1 50")
            continue

        acerto = chute == numero_secreto
        maior  = acerto > numero_secreto
        menor  = acerto < numero_secreto

        if(acerto):    
            print("Você acertou o número e fez {} pontos".format(pontos))
            break
        else:
            if(chute > numero_secreto):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(chute < numero_secreto):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("\nFim do jogo\n")

if(__name__ == "__main__"):
    jogar()