import os 
import math 
import sys
import random 
import re
def countapplesandoranges(s, t, a, b, manzanas, naranjas):
    manzanastotales=naranjastotales=0
    for i in range(len(manzanas)):
        if s<= a+manzanas[i]<=t:
            manzanastotales+=1
    for i in range(len(naranjas)):
        if s<= b+naranjas[i]<=t:
            naranjastotales+=1
    print("en total han caido", str(manzanastotales), "manzanas")
    print("en total han caido", str(naranjastotales), "naranjas")
    if __name__ =='__main__':
        primerinput=input().rstrip().split()
        s=int(primerinput[0])
        t=int(primerinput[1])
        segundoinput=input().rstrip().split()
        a=int(segundoinput[0])
        b=int(segundoinput[1])
        tercerinput=input().rstrip().split()
        x=int(tercerinput[0])
        y=int(tercerinput[1])
        manzanas= list(map(int, input().rstrip().split()))
        naranjas= list(map(int, input().rstrip().split()))
        countapplesandoranges(s, t, a, b, manzanas, naranjas)