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
    def __repr__(self):
        return "(Mase: %d, Max mase: %d, Krovinio mase: %d, Nr: %d)" %(self.mase,self.maxMase,self.krovinioMase,self.nr)    
    def __str__(self):
        return "Mase: %i, Max mase: %i, Krovinio mase: %i, Nr: %i" %(self.mase,self.maxMase,self.krovinioMase,self.nr)

class Traukinys:
    def __init__(self,lok,vag):
        self.lok = lok
        self.vag = vag
    def __repr__(self):
        return "(Lok: %s Vag: %s)" % (self.lok,self.vag)
    def __str__(self):
        return "Lokomotyvo mase: %d,Vagono mase: %d" %(self.lok,self.vag)
    def __add__(self,other):
        lok_mase = self.lok.mase+other.lok.mase
        vag_mase = self.vag.mase+other.vag.mase
        mase = lok_mase + vag_mase
        
        return mase
        #return Traukinys(self.lok.mase+other.lok.mase,self.vag.mase+other.vag.mase)
    def __sub__(self,other):
        maxMaseVagono = self.vag.maxMase+other.vag.maxMase
        maxMaseLokoloko = self.lok.maxMase+other.lok.maxMase
        maxMase = maxMaseVagono + maxMaseLokoloko
        
        krovinioMase = self.vag.krovinioMase + other.vag.krovinioMase 
        
        uzimtaMase = maxMase - krovinioMase
        
        return uzimtaMase
    def __len__(self):
	    return len(Traukinys)
    def __bool__(self):
	    return False

