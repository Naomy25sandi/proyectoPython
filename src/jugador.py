import random


# Lista de colores disponibles
turno_jugador = ["red", "green", "yellow", "blue"]

class Jugador:
    def __init__(self, es_jugador=True) -> None:
        self.es_jugador = es_jugador

    def hacer_intento(self):
       colores_disponibles = ["red", "green", "yellow", "blue"]
       intento = []
print("Ingresa tu intento de colores (red, green, yellow, blue).")
for i in range(4):
            color = input("Ingresa un color: ")
            