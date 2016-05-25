class Lokomotyvas:
    def __init__(self,mase,maxMase):
        self._mase = mase
        self._maxMase = maxMase

    @property
    def mase(self):
        return self._mase
    @property
    def maxMase(self):
        return self._maxMase

    @mase.setter
    def mase(self,value):
        self._mase = value
    @maxMase.setter
    def maxMase(self,value):
        self._maxMase = value
    
    def __add__(self,other):
        return(self._mase+other._mase,self._maxMase+other._maxMase)
        
    def __sub__(self,other):
        return(self._mase-other._mase,self._maxMase-other._maxMase)
        
    def __repr__(self):
        return "(Mase: %d, Max mase: %d)"%(self._mase,self._maxMase)
        
    def __str__(self):
        return "Mase: %i, Max mase: %i" %(self._mase,self._maxMase)

class Vagonas:
    def __init__(self,mase,maxMase,krovinioMase,nr):
        self._mase = mase
        self._maxMase = maxMase
        self._krovinioMase = krovinioMase
        self._nr = nr
    
    @property
    def mase(self):
        return self._mase
    @property
    def maxMase(self):
        return self._maxMase
    @property
    def krovinioMase(self):
        return self._krovinioMase
    @property
    def nr(self):
        return self._nr
    
    @mase.setter
    def mase(self,value):
        self._mase = value
    @maxMase.setter
    def maxMase(self,value):
        self._maxMase = value
    @krovinioMase.setter
    def krovinioMase(self,value):
        self._krovinioMase = value
    @nr.setter
    def nr(self,value):
        self._nr = value
        
    def __add__(self,other):
        return(self.mase+other.mase,self.maxMase+other.maxMase)

    def __repr__(self):
        return "(Mase: %d, Max mase: %d, Krovinio mase: %d, Nr: %d)" %(self.mase,self.maxMase,self.krovinioMase,self.nr)    

    def __str__(self):
        return "Mase: %i, Max mase: %i, Krovinio mase: %i, Nr: %i" %(self.mase,self.maxMase,self.krovinioMase,self.nr)

class Traukinys:
    def __init__(self,lok,vag,nr):
        self.lok = lok
        self.vag = vag
        self.nr = nr
    def __repr__(self):
        return "(Lok: %s Vag: %s Traukinio Nr.: %s)" % (self.lok,self.vag,self.nr)
    def __str__(self):
        return "Lokomotyvo mase: %s,Vagono mase: %s, Traukinio nr.: %s" %(self.lok,self.vag,self.nr)
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

