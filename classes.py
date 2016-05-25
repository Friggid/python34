class Lokomotyvas:
    def __init__(self,mase,maxMase):
        self.mase = mase
        self.maxMase = maxMase

    @property
    def mase(self):
        return self._mase
    @property
    def maxMase(self):
        return self._maxMase

    @mase.setter
    def mase(self,v):
        if (v > 0)and(type(v)==int): 
            self._mase = v
        else:
            self._mase = 1
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Mase turi buti skaicius ir daugiau uz 0!")
            print("Nustatyta pradine reiksme 1!")                        
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")            
    @maxMase.setter
    def maxMase(self,v):
        if (v > 0)and(type(v)==int): 
            self._maxMase = v
        else:
            self._maxMase = 2
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Max mase turi buti skaicius ir daugiau uz 0!")
            print("Nustatyta pradine reiksme 2!")            
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n") 
    
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
        self.mase = mase
        self.maxMase = maxMase
        self.krovinioMase = krovinioMase
        self.nr = nr
    
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
    def mase(self,v):
        if (v > 0)and(type(v)==int): 
            self._mase = v
        else:
            self._mase = 1
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Mase turi buti skaicius ir daugiau uz 0!")
            print("Nustatyta pradine reiksme 1!")            
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n") 
    @maxMase.setter
    def maxMase(self,v):
        if (v > 0)and(type(v)==int): 
            self._maxMase = v
        else:
            self._maxMase = 2
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Max mase turi buti skaicius ir daugiau uz 0!")
            print("Nustatyta pradine reiksme 2!")            
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    @krovinioMase.setter
    def krovinioMase(self,v):
        if (v > 0)and(type(v)==int): 
            self._krovinioMase = v
        else:
            self._krovinioMase = 1
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Krovinio mase turi buti skaicius ir daugiau uz 0!")
            print("Nustatyta pradine reiksme 1!")            
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    @nr.setter
    def nr(self,v):
        if (v > 0)and(type(v)==int): 
            self._nr = v
        else:
            self._nr = 1
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Nr turi buti skaicius ir daugiau uz 0!")
            print("Nustatyta pradine reiksme 1!")            
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        
    def __add__(self,other):
        return(self._mase+other._mase,self._maxMase+other._maxMase)

    def __repr__(self):
        return "(Mase: %d, Max mase: %d, Krovinio mase: %d, Nr: %d)" %(self._mase,self._maxMase,self._krovinioMase,self._nr)    

    def __str__(self):
        return "Mase: %i, Max mase: %i, Krovinio mase: %i, Nr: %i" %(self._mase,self._maxMase,self._krovinioMase,self._nr)
#Add ir Sub surusiuoja traukinius pagal laisva vieta arba visa vagonu ir lokomatyvu mase
class Traukinys:
    def __init__(self,lok,vag,nr):
        self.lok = lok
        self.vag = vag
        self.nr = nr
    def __repr__(self):
        return "(Lok: %s Vag: %s Traukinio Nr.: %s)" % (self.lok,self.vag,self.nr)
    def __str__(self):
        return "Lokomotyvo mase: %s,Vagono mase: %s, Traukinio nr.: %s" %(self.lok,self.vag,self.nr)
    #1.Rusiuojant pagal mase suskaiciuoja bendra lokomatyvu ir vagonu mase ir isrusiuoja didejimo tvarka
    def __add__(self,other):
        lok_mase = self.lok._mase+other.lok._mase
        vag_mase = self.vag._mase+other.vag._mase
        mase = lok_mase + vag_mase
        
        return mase
    #2.Rusiuojant pagal laisva vieta pirmiausia suranda maksimalia vagonu ir lokomatyvu mase
    #  Tada is maksimalios mases atima vezama kroviniu mase ir randama atlikusi laisva vieta
    def __sub__(self,other):
        maxMaseVagono = self.vag._maxMase+other.vag._maxMase
        maxMaseLokoloko = self.lok._maxMase+other.lok._maxMase
        maxMase = maxMaseVagono + maxMaseLokoloko
        
        krovinioMase = self.vag._krovinioMase + other.vag._krovinioMase 
        
        uzimtaMase = maxMase - krovinioMase
        
        return uzimtaMase
    def __len__(self):
	    return len(Traukinys)
    def __bool__(self):
	    return False

