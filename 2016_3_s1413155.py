class Lokomotyvas:
    def __init__(self,mase,maxMase):
        self.mase = mase
        self.maxMase = maxMase
    def __add__(self,other):
        return(self.mase+other.mase,self.maxMase+other.maxMase)
    def __sub__(self,other):
        return(self.mase-other.mase,self.maxMase-other.maxMase)
    def __repr__(self):
        return "(Mase: %d, Max mase: %d)"%(self.mase,self.maxMase)
    def __str__(self):
        return "Mase: %i, Max mase: %i" %(self.mase,self.maxMase)

class Vagonas:
    def __init__(self,mase,maxMase,krovinioMase,nr):
        self.mase = mase
        self.maxMase = maxMase
        self.krovinioMase = krovinioMase
        self.nr = nr
    def __add__(self,other):
        return(self.mase+other.mase,self.maxMase+other.maxMase)
    def __str__(self):
        return "Mase: %i, Max mase: %i, Krovinio mase: %i, Nr: %i" %(self.mase,self.maxMase,self.krovinioMase,self.nr)

class Traukinys:
    def __init__(self,lok,vag):
        self.lok = lok
        self.vag = vag
    def __repr__(self):
        return "Lok: %s Vag: %s" % (self.lok,self.vag)
    def __str__(self):
        return "Lokomotyvo mase: %d,Vagono mase: %d" %(self.lok,self.vag)
    def __add__(self,other):
        trauk_mase = self.lok.mase+other.lok.mase
        vag_mase = self.vag.mase+other.vag.mase
        mase = trauk_mase + vag_mase
        
        return mase
        #return Traukinys(self.lok.mase+other.lok.mase,self.vag.mase+other.vag.mase)
    def __sub__(self,other):
        maxMaseVagono = self.vag.maxMase+other.vag.maxMase
        maxMaseLokoloko = self.lok.maxMase+other.lok.maxMase
        maxMase = maxMaseVagono + maxMaseLokoloko
        
        uzimtaVagonu = self.vag.krovinioMase + other.vag.krovinioMase 
        
        uzimtaMase = maxMase - uzimtaVagonu
        
        return uzimtaMase
    def __len__(self):
	    return len(Traukinys)
    def __bool__(self):
	    return False
            
Lok1 = Lokomotyvas(1,10)
Lok2 = Lokomotyvas(13,20)
Lok3 = Lokomotyvas(2,5)
Lok4 = Lokomotyvas(20,30)
Vag1 = Vagonas(5,10,3,1)
Vag2 = Vagonas(9,20,7,2)
Vag3 = Vagonas(9,20,10,3)
Vag4 = Vagonas(8,20,9,4)

Trauk1 = Traukinys(Lok1,Vag1)
Trauk2 = Traukinys(Lok2,Vag2)
Trauk3 = Traukinys(Lok3,Vag3)
Trauk4 = Traukinys(Lok4,Vag4)

Laisva1 = (Trauk1-Trauk2) - (Trauk1+Trauk2)
Laisva2 = (Trauk3-Trauk4) - (Trauk3+Trauk4)
print(Laisva1)
print(Laisva2)


# Sastatas = Vag+Vag2

# Traukinys1 = Traukinys(Lokomotyvas2,Vag)
# Traukinys2 = Traukinys(Lokomotyvas1,Vag2)

# TraukMase = Traukinys1+Traukinys2
# TraukUzimta = Traukinys1-Traukinys2 
# laisva = TraukMase - TraukUzimta
#14,6
# add(14+6,kroviniomase)
#print(TraukMase)
#print(TraukUzimta)
#print(laisva)

#{"vagonas": [{"nr": 1, "mase": 20, "maxMase": 40, "krovinioMase": 10}], "lokomotyvas": [{"maxMase": 3, "mase": 2}, {"maxMase": 1, "mase": 1}]}

# lok.mase+vag.mase+vag.krovinioMase = Traukinio mase
# vag.maxMase+lok.maxMase = Max traukinio mase
# Max traukinio mase - traukinio mase = laisva vieta
