# proyectoPython
Empecé creando mi proyecto separándolo en 3 partes: Tablero, Jugador y main. Creación de Tablero para darle la funcionalidad al mismo y así poder tener una base para empezar mi proyecto. En el mismo, creé la clase Tablero y se importa el colored. Guardé los colores en un diccionario e inicialicé el constructor sin definir los parámetros para no limitar mi clase, creando dentro de ella arreglos vacíos que voy a necesitar más adelante.

Creé los métodos de mi clase Tablero: definir_color, al cual le envío el parámetro color y guardo mi atributo color en la variable que era un arreglo vacío creado anteriormente.

El método validar_ganador asigna el atributo de intento y crea una variable Retroalimentacion con un arreglo vacío. Dentro de este método, creo otra variable para poder manipular mi arreglo color_secreto, de esta manera puedo iterar y comprobar si copia_color cumple los requisitos para ser color_verde, color_amarillo o color_blanco.

Creé el método mostrar, que recorre los intentos y la retroalimentación. Construye una línea para los colores del intento y otra para la retroalimentación. Imprime ambas líneas juntas para mostrar el resultado en pantalla.

Por último, el método actualizar_tablero añade un nuevo intento y su retroalimentación a la lista de turnos.

Luego, creé el archivo jugador que contiene la lógica con la clase Jugador, en la que almaceno la lista de colores a elegir, inicializando el atributo con un estado en True y creo una variable. Además, defino la lógica del adivinador usando la clase Jugador como parámetro, así podemos usar el atributo con el estado que necesito para asignarle a cada clase.

Creé la clase Creador, que es la lógica de la Computadora. Aquí hago uso del import de random, también implemento el uso de .split(), que divide la cadena de entrada en una lista de colores, y .strip(), que elimina cualquier espacio extra al principio o al final de la entrada.

En el main, importo a Tablero y uso la clase Tablero. Creo la clase Juego, que representa el contexto general del juego. La inicializo y creo una variable que almacena mi clase Tablero, además se agregaron atributos. Uso None para indicar que el constructor no devuelve ningún valor.

self.creador_codigo: está vacío (None). Este atributo se usará para almacenar quién crea el código en el juego.
self.adivinador_codigo: está vacío (None). Este atributo se usará para almacenar quién intenta adivinar el código en el juego.
Creamos el siguiente método: elegir_turno y se crea una variable para almacenar la información ingresada en el input y así definir la lógica de quién va a jugar primero.

En el método jugadas_turnos está la lógica para saber si el usuario o la máquina ganaron o perdieron en cuanto a los intentos realizados.

iniciar_juego: Prepara y comienza el juego llamando a otros métodos que configuran los turnos y manejan las jugadas.
elegir_turno: Configura los turnos para los jugadores.
jugadas_turnos: Maneja la lógica del juego durante las jugadas o turnos.

