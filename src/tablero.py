from colored import fg,attr
# Importamos colored fg=para los colores y attr para reiniciar el color
# Creacion de Tablero los colores los agrego usando un diccionario
class Tablero:
    colores = {
        "r": fg("red"),
        "g": fg("green"),
        "y": fg("yellow"),
        "b": fg("blue")
    }
    
    def __init__(self)-> None: # el constructor no se definen los valores para no limitarla
        self.color_secreto= []# se crean arreglos vacios
        self.turnos= []
    
    def definir_color(self, color):# metodo donde pasamos el color secreto
        self.color_secreto = color # el color lo guardamos en esta variable
    
    def validar_ganador(self, intento):
        retroalimentacion=[]# arreglo vacio 
        copia_color= self.color_secreto # creamos una variable para guardar el valor del color secreto
        for i in range(4):# ocupamos comprobar iterar
                if intento[i] == copia_color[i]:
                    retroalimentacion.append("color_verde")# se guarda en retroalimentacion y se comparan los datos
                    copia_color[i]=None # para quitar la opcion que se reviso y continuar con la siguiente
                elif intento[i] in copia_color:
                    retroalimentacion.append("color_amarillo")
                    copia_color.remove(intento[i])# se elimina 
                else: retroalimentacion.append("color_blanco")
        return retroalimentacion # retornamos la lista
    
    def mostrar(self): # se crea otro metodo
            for intento, retroalimentacion in self.turnos:
                fila_color = " ".join([self.colores[color]+"🟠"+attr("reset")for color in intento])
                #join recorremos la lista de colores y el comprehension list
                fila_retroalimentacion = " ".join([
                    fg(2) + "🟠" + attr("reset") if adivina == "color_verde"
                    
                    else fg(3) + "🟠" + attr("reset") if adivina == "color_amarillo"
                    
                    else "🟠"
                    
                    for adivina in retroalimentacion
                ])
                
                print(f"{fila_color} {fila_retroalimentacion}")
                
 