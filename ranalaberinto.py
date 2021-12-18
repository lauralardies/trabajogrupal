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