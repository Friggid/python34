import json
import sys
import classes
from classes import * 

def readJson():
    #failas = input()
    with open("data.json") as data_file:
        data=json.load(data_file)
    
    lok = []
    vag = []
    trauk = []
    for i in range(len(data["lokomotyvas"])):
        lok.append(Lokomotyvas(data['lokomotyvas'][i]['mase'],data['lokomotyvas'][i]['maxMase']))
    
    for i in range(len(data["vagonas"])):
        vag.append(Vagonas(data['vagonas'][i]['nr'],data['vagonas'][i]['mase'],data['vagonas'][i]['maxMase'],data['vagonas'][i]['krovinioMase']))
    
    trauk.append(Traukinys(lok[0],vag[0],0))
    trauk.append(Traukinys(lok[1],vag[1],1))
    trauk.append(Traukinys(lok[2],vag[2],2))
    return trauk

def showTrains():
    trauk = []
    trauk = readJson()
    for j in range(len(trauk)):
        print("Traukinys: ", j+1)
        print(trauk[j])
        print("----------------------------------------------------")
    
def sorting():      
    trauk = []
    trauk = readJson()
    
    sortSelect = input("\nPasirinkite rusiavimo tipa:\n1.Laisva vieta traukinyje, 2.Mase: ")
    if(sortSelect=="1"):
        Laisva = []
        Laisva.append(((trauk[0]+trauk[1]) - (trauk[0]-trauk[1]),0))
        Laisva.append(((trauk[1]+trauk[2]) - (trauk[1]-trauk[2]),1))
        Laisva.append(((trauk[2]+trauk[0]) - (trauk[2]-trauk[0]),2))
        Laisva = sorted(Laisva,reverse=False)
        for i in range(len(Laisva)):
            for j in range(len(trauk)):
                if (Laisva[i][1]==trauk[j].nr):
                    print("----------------------------------------------------")
                    print("Laisva vieta traukinyje: ",Laisva[i][0])
                    print("Traukinys: ",trauk[j])
    elif(sortSelect=="2"):
        Mase = []
        Mase.append((trauk[0]+trauk[1],0))
        Mase.append((trauk[1]+trauk[2],1))
        Mase.append((trauk[2]+trauk[0],2))
        Mase = sorted(Mase,reverse=False)
        for i in range(len(Mase)):
            for j in range(len(trauk)):
                if(Mase[i][1]==trauk[j].nr):
                    print("----------------------------------------------------")
                    print("Visa traukinio mase: ",Mase[i][0])
                    print("Traukinys: ",trauk[j])
    else:
        print("Yveskite skaiciu 1 arba 2.")
   
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

def writeJson():
#failas = input()
             ## '/mif/stud3/2014/tami1864/Python/3atsisk/'+ cia failas turi but
    with open("data.json") as data_file:
        data=json.load(data_file)

    tipas = input("1. Lokomotyvas, 2. Vagonas. Parasykite pasirinkima: ")

    if(tipas=="1"):
        tipas="lokomotyvas"

        mase = input("Yveskite mase: ")
        maxMase = input("Yveskite max mase: ")

        isvedimDuom = {'mase':int(mase),'maxMase':int(maxMase)}
        data[tipas].append(isvedimDuom)
#/mif/stud3/2014/tami1864/Python/3atsisk/
        with open('data.json', 'w') as outfile:
            json.dump(data,outfile)
        print(data)

    elif(tipas=="2"):
        tipas="vagonas"

        mase=input("Yveskite mase: ")
        maxMase=input("Yveskite max mase: ")
        krovinioMase=input("Yveskite krovinio mase: ")
        nr=input("Yveskite krovinio numeri: ")

        isvedimDuom = {'mase':int(mase),'maxMase':int(maxMase),'krovinioMase':int(krovinioMase),'nr':int(nr)}
        data[tipas].append(isvedimDuom)
#/mif/stud3/2014/tami1864/Python/3atsisk/
        with open('data.json', 'w') as outfile:
            json.dump(data,outfile)
        print(data)

    else:
        print("Neteisingas pasirinkimas")
        sys.exit(0)

print("----------------------------------------------------")
print("|               PROGRAMOS NAUDOJIMAS               |")
print("|                                                  |")
print("| 1. Yveskite failo pavadinima                     |")
print("| 2. Pasirinkite norima veiksma                    |")
print("| 3. Skaityti/rasyti JSON, rusiuoti                |")
print("| 4. Rusiuokite faila pagal 2 kriterijus           |")
print("----------------------------------------------------")
print("\n")
print("----------------------------------------------------")
print("|                      MENIU                       |")
print("|                                                  |")
print("|    Yveskite failo pavadinima                     |")
print("| 1. Paziurekite esamus traukinius                 |")
print("| 2. Rusiuokite esamus traukinius                  |")
print("| 3. Pridekite nauja vagona ar lokomotyva          |")
print("| Q. Iseiti is programos                           |")
print("----------------------------------------------------")

print("----------------------------------------------------")
def menu():
    menuPick = input("Pasirinkimas(1,2,3,Q): ")    
    if(menuPick == "1"):
        showTrains()
        menu()
    elif(menuPick == "2"):
        sorting()
        menu()
    elif(menuPick == "3"):
        writeJson()
        menu()
    else:
        print("Programa sustabdyta.")
        sys.exit(0)
        
menu()