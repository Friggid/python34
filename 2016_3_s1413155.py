import readwrite
from readwrite import *

class Lokomotyvas:
    def __init__(self,mase,maxMase):
        self.mase = mase
        self.maxMase = maxMase
    def __add__(self,other):
        return(self.mase+other.mase,self.maxMase+other.maxMase)
    def __sub__(self,other):
        return(self.mase-other.mase,self.maxMase-other.maxMase)
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

class Traukinys:
    def __init__(self,lok,vag):
        self.lok = lok
        self.vag = vag
    def __repr__(self):
        return "Lok: %s Vag: %s" % (self.lok,self.vag)
    def __str__(self):
        return "Lokomatyvas: %d Vagonas: %d" % (self.lok,self.vag)
    def __add__(self,other):
        return Traukinys(self.lok.mase+other.lok.mase,self.vag.mase+other.vag.mase)
    def __sub__(self,other):
        return Traukinys(self.lok.mase-other.lok.mase,self.vag.mas-+other.vag.mase)
    def __len__(self):
		return len(Traukinys)
    def __bool__(self):
		return False
            
Lokomotyvas1 = Lokomotyvas(1,2)
Lokomotyvas2 = Lokomotyvas(13,3)
Vag = Vagonas(1,2,3,4)

Traukinys1 = Traukinys(Lokomatyvas1,Vag)

print(Traukinys1)
