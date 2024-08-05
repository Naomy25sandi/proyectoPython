import random
#choice()
#La función choice(sec) devuelve un elemento aleatorio de una secuencia. Es muy útil cuando hay que elegir al azar un elemento de entre un conjunto
turno_jugador= [ "red", "green", "yellow","blue"]
for i in range(4):
 print(random.choice(turno_jugador))
