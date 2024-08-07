import random # se importa el random
# Lista de colores disponibles


class Jugador:
    colores_disponibles = ["red", "green", "yellow", "blue"]
    def __init__(self, es_jugador=True) -> None:
        self.es_jugador = es_jugador
# inicializamos el atributo con el estado de True 
 # se crea la logica de jugador y de la maquina
 # Tenemos 2 clases la que adivina y el creador sabemos de quien es el turno por el estado con quien inicia el juego
class Adivinar(Jugador):# llamamos ala clase Jugador para saber quien inicia el juego
      def hacer_adivinanza(self):
          if self.es_jugador:
              color_adivinar = input("Ingrese el color a adivinar: (red green yellow blue)").strip().split()
              return color_adivinar 
          else:
              color_adivinar = random.choices(self.colores_disponibles,k=4)
              return color_adivinar # usamos el random para dar una lista aleatoria de las opciones de los colores        


class Creador(Jugador):
      def hacer_creador(self):
          if self.es_jugador:
              color_adivinar = input("Ingrese el color a crear: (red green yellow blue)").strip().split()
              return color_adivinar
          else:
              color_crear = random.choices(self.colores_disponibles,k=4)
              return color_crear
  