import random

incogito = random.randint(1, 100)


def bienvenido():
    print("Bienvenido al juego de adivinanza")


def juego_adivina():
    bienvenido()
    while True:
        x = input("Ingresa un numero: ")
        if x.lower() == "salir":
            print("Saliendo...")
            break
        x = int(x)
        print(" ")
        if x == incogito:
            print("Felicidades has adivinado")
            print(" ")
            break
        if 1 <= x <= 100:
            print("Error! Vuelve intentarlo.")
            print(" ")
        else:
            print("Valor invalido!")
            break


print(incogito)
juego_adivina()
