import readwrite
from readwrite import *

class Lokomotyvas:
    def __init__(self,mase,maxMase):
        self.mase = mase
        self.maxMase = maxMase
    def __add__(self,other):
        return(self.mase+other.mase,self.maxMase+other.maxMase)

    def __repr__(self):
        return "(Mase: %d,%d)"%(self.mase,self.maxMase)
    def __str__(self):
        return "Mase: %i, Max mase: %i" %(self.mase,self.maxMase)

class Vagonas:
    def __init__(self,mase,maxMase,krovinioMase,nr):
        self.mase = mase
        self.maxMase = maxMase
        self.krovinioMase = krovinioMase
        self.nr = nr
    def __str__(self):
        return "Mase: %i, Max mase: %i, Krovinio mase: %i, Nr: %i" %(self.mase,self.maxMase,self.krovinioMase,self.nr)

Lokomotyvas1 = Lokomotyvas(1,2)
Lokomotyvas2 = Lokomotyvas(13,3)
Vag = Vagonas(1,2,3,4)

lokas = Lokomotyvas(0,0)

lokas = Lokomotyvas1 + Lokomotyvas2
print(lokas)
