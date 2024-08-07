from tablero import Tablero
from jugador import Adivinar, Creador # importo adivinar y creador del archivo jugador
# importamos nuestras clases Tablero y Jugador para poder usarlas
 
class Juego:
    def __init__(self) -> None: # constructor inicializo
        self.tablero = Tablero() # 
        self.creador_codigo = None
        self.adivinador_codigo = None
        
    
    # preguntamos y creamos un metodo
    def elegir_turno(self):# creamos una variable para el input, recibir la informacion
        pregunta = input("Quieres ser el adivinador o el creador? c - a: ").lower().strip()
        if pregunta == "c":
            self.creador_codigo = Creador(True)# almaceno los atributos importados en estas variables
            self.adivinador_codigo= Adivinar(False)# dandoles un estado para poder verificar de quien es el turno
        else:
            self.creador_codigo = Creador(False)
            self.adivinador_codigo = Adivinar(True)
            
        self.tablero.definir_color(self.creador_codigo.hacer_creador())
      
       
    def jugadas_turnos(self):# creo otro metodo
        for turnos in range(12):
            intento = self.adivinador_codigo.hacer_adivinanza()
            retroalimentacion = self.tablero.validar_ganador(intento)
            self.tablero.actualizar_tabla(intento,retroalimentacion)
            self.tablero.mostrar()
            print(turnos)
            if retroalimentacion == ["color_verde"]*4:
                print("Felicidades haz ganado!")
                return
        
        print("Perdiste!")

    
    def iniciar_juego(self):# creo otro metodo
        self.elegir_turno()
        self.jugadas_turnos()


if __name__ == "__main__":
    juego = Juego()
    juego.iniciar_juego()
        