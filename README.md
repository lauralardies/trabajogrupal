# trabajogrupal

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/trabajogrupal)
https://github.com/lauralardies/trabajogrupal

Para este trabajo hemos realizado 8 programas distintos.

Ejercicio 1: Suma simple de una matriz.
Usamos la funcion simpleArraySum para obtener la suma de los todos los elementos de una matriz, que ademas tienen que ser valores enteros.
```
Ejercicio 2: Compara los problemas.
Se comparan las puntuaciones obtenidas en 3 apartados entre Lucia y Carlos, el que obtenga mas puntuacion en algun apartado gana una punto. Gana el que mas puntos tenga
```
Ejercicio 3: Una suma muy grande.
Calcular e imprimir la suma de los elementos en una matriz, teniendo en cuenta que algunos de esos números enteros pueden ser bastante grandes.
```
def sumaGrande(ar):
    sum = 0
    for i in range(len(ar)):
        sum = sum + ar[i]
    return sum

ar = [164318575843289072592317093673840167348146313258578542, 6723956194536770435893417961029510045, 7789247418956438904345745643704561326405, 347196527414380508235068233333651970480190482, 674297478423456798756148792359658339020184219, 432364536371846045754730173580113413337578314590987657892630, 32396582905331859175187159197571672167138480134, 527895426247913048266382948625312682014756628, 107573598625772850912742639457291357825, 4158735873364178950231254782301205738713584, 8189564137631921345679280592153263948754264194169, 86574175973407909146135687918501581724153218041256326019121, 142145679128579136563425524692158030531753385197364523, 543851985196451268479802357794767145421547683795876312557923584657351042]
sum = sumaGrande(ar)
sum = f'{sum:,}'
print("The sum of all the elements of this array is: " + str(sum))
```
Ejercicio 4: La escalera.
Imprimir una escalera de tamaño n.
```
def escalera(n):
    for numAlmohadillas in range(1, n + 1):
        print(" "*(n - numAlmohadillas) + "# "*numAlmohadillas)

n = int(input("¿De qué tamaño quieres que sea tu escalera?: "))
escalera(n)
```
Ejercicio 5: Juego de piedras.
Dos jugadores tienen que eliminar de forma que el jugador que no pueda eliminar en algun turno pierde, en cada turno se pueden eliminar 2, 3 o 5 piedras.
```
Ejercicio 6: Rana en laberinto.
Escribir un programa que calcule e imprima una probabilidad de que Alef escape del laberinto.
```
import random

class Laberinto():
    def __init__(self) -> None:
        self.coordenadas = (
                    (0,1), 
                    (0,2), 
                    (0,3),
                    (0,4),
                    (0,5),
                    (0,6),
                    (0,7),
                    (0,8),
                    (0,9),
                    (1,8),
                    (2,1), 
                    (2,3), 
                    (2,4),
                    (2,8),
                    (3,1), 
                    (3,4),
                    (3,8),
                    (4,1),
                    (4,3), 
                    (4,4), 
                    (4,5),
                    (4,6), 
                    (5,3), 
                    (5,5),
                    (5,7),
                    (5,8), 
                    (6,3),
                    (6,5),
                    (6,8),
                    (7,2),
                    (7,3),
                    (7,5),
                    (8,2),
                    (8,5),
                    (9,2),
                    (9,5),
                    )
        self.minas = (
                (1,7),
                (2,5),
                (6,6),
                (7,4),
                (7,8),
                (8,1),
                (8,7),
                (9,3),
                )
        self.start = [0,0]
        self.finish = [6,7]
        self.posicion = self.start
        self.tunel = (
                    (3,3,5,4),
                    (9,1,8,3),
                    (6,4,1,9),
                    (9,4,8,9),
                    )
        self.status = "vivo"
        self.laberinto = []
        self.movimientos = []

    def crearLaberinto(self):
        for x in range(10):
            fila = []
            for y in range(10):
                if tuple([x, y]) in self.coordenadas:
                    fila.append("#")
                elif list([x, y]) == self.start:
                    fila.append("A")
                elif list([x, y]) == self.finish:
                    fila.append("%")
                elif tuple([x, y]) in self.minas:
                    fila.append("O")
                else:
                    fila.append(" ")
            self.laberinto.append(fila)

    def printLaberinto(self):
        print(self.laberinto[0])
        print(self.laberinto[1])
        print(self.laberinto[2])
        print(self.laberinto[3])
        print(self.laberinto[4])  
        print(self.laberinto[5])    
        print(self.laberinto[6])    
        print(self.laberinto[7])    
        print(self.laberinto[8])    
        print(self.laberinto[9])    

    def empezarCero(self):
        self.posicion = self.start
        self.status = "vivo"
        self.movimientos = []

    def opcionRandom(self):
        opcion = random.randint(1,4)
        if opcion == 1:
            opcion = "Abajo"
        if opcion == 2:
            opcion = "Arriba"
        if opcion == 3:
            opcion = "Derecha"
        if opcion == 4:
            opcion = "Izquierda"
        
        return opcion

    def posicionValida(self, x, y):
        if (x < 0) | (y < 0):
            return False
        if (x > 9) | (y > 9):
            return False
        if self.laberinto[x][y] == "#":
            return False
        return True

    def posicionTunel(self, tunelsalida):        
        for i in range(len(self.tunel)):
            t = self.tunel[i]
            if t[0] == self.posicion[0] and t[1] == self.posicion[1]:
                tunelsalida = [t[2], t[3]]
                return tunelsalida
            if t[2] == self.posicion[0] and t[3] == self.posicion[1]:
                tunelsalida = [t[0], t[1]]                
                return tunelsalida
        return False

    def posicionJugador(self):
        tunelsalida = [0,0]
        if self.posicionValida(self.posicion[0], self.posicion[1]):
            if self.laberinto[self.posicion[0]][self.posicion[1]] != "O":
                if self.laberinto[self.posicion[0]][self.posicion[1]] != "%":
                    if self.posicionTunel(tunelsalida) == False:
                        self.laberinto[self.posicion[0]][self.posicion[1]] = "A"
                    else:
                        tunelsalida = self.posicionTunel(tunelsalida)
                        self.posicion[0] = tunelsalida[0]
                        self.posicion[1] = tunelsalida[1]
                        self.laberinto[tunelsalida[0]][tunelsalida[1]] = "A"

    def posicionAnterior(self):
        self.laberinto[self.posicion[0]][self.posicion[1]] = " "
        
    def resolverLaberinto(self):

        while len(self.movimientos) >= 0:
            movement = str(self.opcionRandom())
            movement = movement.capitalize() 

            if movement == "Abajo":
                if self.posicionValida(self.posicion[0] + 1, self.posicion[1]) == True:
                    self.movimientos.append("Abajo")
                    self.posicionAnterior()
                    self.posicion = [self.posicion[0] + 1, self.posicion[1]]
                    self.posicionJugador()

            if movement == "Arriba":
                if self.posicionValida(self.posicion[0] - 1, self.posicion[1]) == True:
                    self.movimientos.append("Arriba")
                    self.posicionAnterior()
                    self.posicion = [self.posicion[0] - 1, self.posicion[1]]
                    self.posicionJugador()
                    
            if movement == "Derecha":
                if self.posicionValida(self.posicion[0], self.posicion[1] + 1) == True:
                    self.movimientos.append("Derecha")
                    self.posicionAnterior()
                    self.posicion = [self.posicion[0], self.posicion[1] + 1]
                    self.posicionJugador()

            if movement == "Izquierda":
                if self.posicionValida(self.posicion[0], self.posicion[1] - 1) == True:
                    self.movimientos.append("Izquierda")
                    self.posicionAnterior()
                    self.posicion = [self.posicion[0], self.posicion[1] - 1]            
                    self.posicionJugador()

            if self.laberinto[self.posicion[0]][self.posicion[1]] == "O":
                self.status = "muerto"
                break

            if self.laberinto[self.posicion[0]][self.posicion[1]] == "%":
                break

laberinto = Laberinto()
laberinto.crearLaberinto()
laberinto.printLaberinto()
resultado = 0
for i in range(100000):
    laberinto.resolverLaberinto()
    if laberinto.status == "vivo":
        resultado =+ 1
    laberinto.empezarCero()

probabilidad = resultado/100000
print("La probabilidad de que Alef escape de este laberinto es de " + str(probabilidad) + ".")
```
Ejercicio 7: Estudiantes de calificación.
Dado el valor inicial de la nota para cada uno de los n estudiantes, escriban código para automatizar el proceso de redondeo.
```
def calificandoEstudiantes(calificaciones):
    calificaciones_redondeadas = []
    for i in range(len(calificaciones)):
        if calificaciones[i] > 40:
            x = [int(n) for n in str(calificaciones[i])]
            if x[1] != 5 and x[1] != 0:
                if x[1] > 5:
                    redondeo = str(x[0] + 1) + "0"
                    if int(redondeo) - calificaciones[i] < 3:
                        calificaciones_redondeadas.append(int(redondeo))
                    else: 
                        calificacion = str(x[0]) + str(x[1])
                        calificaciones_redondeadas.append(int(calificacion))
                else:
                    redondeo = str(x[0]) + "5"
                    if int(redondeo) - calificaciones[i] < 3:
                        calificaciones_redondeadas.append(int(redondeo))
                    else: 
                        calificacion = str(x[0]) + str(x[1])
                        calificaciones_redondeadas.append(int(calificacion))
            else:
                calificaciones_redondeadas.append(calificaciones[i])
        else:
            calificaciones_redondeadas.append(calificaciones[i])
    return calificaciones_redondeadas

calificaciones = []
c = int(input("Introduce el número de calificaciones que has evaluado: "))
# Si hay cinco calificaciones, introduces el número 5 y después de darle al Enter introduces una a una las calificaciones sobre 100.

for i in range (c):
    n = int(input())
    calificaciones.append(n)

calificaciones_redondeadas = calificandoEstudiantes(calificaciones)
print("Las calificaciones de los estudiantes han sido las siguientes: " + str(calificaciones))
print("Las calificaciones redondeadas de los estudiantes son las siguientes: " + str(calificaciones_redondeadas))
```
Ejercicio 8. Manzana y Naranja.
Con la funcion countapplesandorangescontamos el numero de naranjas y manzanas que caen en la casa de Sam, sabiendo la distancia de los arboles a las casa y cuanto se desplazan las frutas
```
