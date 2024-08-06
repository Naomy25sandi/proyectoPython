from tablero import Tablero
from jugador import Jugador
from maquina import Maquina

def main():
    # Crear una instancia del tablero y definir el color secreto
    tablero = Tablero()
    tablero.definir_color(["r", "g", "b", "y"])  # Ejemplo de color secreto
    
    # Crear una instancia del jugador y de la máquina
    jugador = Jugador()
    maquina = Maquina()
    
    # El jugador y la máquina juegan
    jugador.jugar(tablero)
    maquina.jugar(tablero)
    
    # Mostrar los resultados finales
    tablero.mostrar()

if __name__ == "__main__":
    main()
