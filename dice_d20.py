import random

resposta = "s"

while resposta == "s":

    input("Aperte Enter para continuar...")

    dado = random.randint(1, 20)
    print("O dado caiu em:", dado)

    if dado == 20:
        print("You have obtained a grimoire!")
    else:
        print("You didn't get a grimoire!")

    resposta = input("Quer girar novamente? s ou n: ")

print("See you!")


