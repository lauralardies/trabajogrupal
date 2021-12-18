import math
import re
import sys
import os
import random
def simplearraysum(ar):
    suma=0
    for number in ar:
        suma=suma+number
    return suma
n=int(input("por favor introduce la lista de dimensiones de la matriz: "))
print("por favor introduce una lista de numeros", end="")
ar=list(map(int,input().rstrip().split()))
print(ar)
resultado=simplearraysum(ar)
print("el valor de la suma es: ", resultado)