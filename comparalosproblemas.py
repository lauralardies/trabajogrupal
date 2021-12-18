import math
from random import randint
lucia1=randint(0,10)
lucia2=randint(0,10)
lucia3=randint(0,10)
carlos1=randint(0,10)
carlos2=randint(0,10)
carlos3=randint(0,10)
print("la puntuacion de lucia es: ")
print("claridad={}".format(lucia1))
print("originalidad={}".format(lucia2))
print("dificultad={}".format(lucia3))
print("la puntuacion de carlos es: ")
print("claridad={}".format(carlos1))
print("originalidad={}".format(carlos2))
print("dificultad={}".format(carlos3))
def compareTiples():
    puntoslucia=0
    puntoscarlos=0
    if lucia1<carlos1:
        puntoscarlos+=1
    elif lucia1>carlos1:
        puntoslucia+=1
    else:
        pass
    if lucia2>carlos2:
        puntoslucia+=1
    elif lucia2<carlos2:
        puntoscarlos+=1
    else:
        pass
    if lucia3<carlos3:
        puntoscarlos+=1
    elif lucia3>carlos3:
        puntoslucia+=1
    else:
        pass
    print("en total lucia tiene", lucia1+lucia2+lucia3, "puntos")
    print("en total carlos tiene", carlos1+ carlos2+carlos3, "puntos")
    return
if carlos1+carlos2+carlos3>lucia1+lucia2+lucia3:
    print("el ganador ha sido carlos")
if lucia1+lucia2+lucia3>carlos1+carlos2+carlos3:
    print("la ganadora ha sido lucia")
if lucia1+lucia2+lucia3==carlos1+carlos2+carlos3:
    print("el juego ha acabado en empate")