import random

from datetime import datetime


def numero_aleatorio():
    return random.randint(1, 50)


def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 100: "))
            if 1 <= numero <= 100:
                return numero
            else:
                print("El número está fuera del del rango del 1 al 100. Pruebe otro.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


def adivina():
    num_aleatorio = numero_aleatorio()
    print("¡Bienvenido al juego 'Acierta el número'!")
    print("Escoja un número entre 1 y 100.")
    while True:
        intento = pedir_numero()
        if intento == num_aleatorio:
            print("¡Has ganado!")
            print("Fecha y hora de acierto:", datetime.now().strftime("%d/%m %H:%M"))
            break
        elif intento < num_aleatorio:
            print("El número es mayor.")
        else:
            print("El número es menor.")


def funcionA(funcionB):
    def funcionC():
        print("¡Adivina el número!")
        funcionB()
        print("¡Gracias por jugar!")
    return funcionC
