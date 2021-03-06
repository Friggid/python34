import json
import sys
import classes
from classes import * 

#Nuskaito json faila y lokomatyvus ir vagonus ir sudaro traukiny.
def readJson():
    with open(failas) as data_file:
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
#Parodo visus traukinius
def showTrains():
    trauk = []
    trauk = readJson()
    print("----------------------------------------------------")
    print("|           Spauzdinamai visi traukiniai           |")    
    print("----------------------------------------------------")
    for j in range(len(trauk)):
        print("Traukinys: ", j+1)
        print(trauk[j])
        print("----------------------------------------------------")

def sorting():      
    trauk = []
    trauk = readJson()
    
    sortSelect = input("\nPasirinkite rusiavimo tipa:\n1.Laisva vieta traukinyje, 2.Mase: ")
    if(sortSelect=="1"):
        print("----------------------------------------------------")
        print("|       Spauzdinama laisva vieta traukinyje        |")    
        print("----------------------------------------------------")
        Laisva = []
        Laisva.append(((trauk[0]+trauk[1]) - (trauk[0]-trauk[1]),0))
        Laisva.append(((trauk[1]+trauk[2]) - (trauk[1]-trauk[2]),1))
        Laisva.append(((trauk[2]+trauk[0]) - (trauk[2]-trauk[0]),2))
        Laisva = sorted(Laisva,reverse=False)
        for i in range(len(Laisva)):
            for j in range(len(trauk)):
                if (Laisva[i][1]==trauk[j].nr):                
                    print("Laisva vieta traukinyje: ",Laisva[i][0])
                    print("Traukinys: ",trauk[j])
                    print("----------------------------------------------------")                    
    elif(sortSelect=="2"):
        print("----------------------------------------------------")
        print("|         Spauzdinama visa traukinio mase          |")    
        print("----------------------------------------------------")
        Mase = []
        Mase.append((trauk[0]+trauk[1],0))
        Mase.append((trauk[1]+trauk[2],1))
        Mase.append((trauk[2]+trauk[0],2))
        Mase = sorted(Mase,reverse=False)
        for i in range(len(Mase)):
            for j in range(len(trauk)):
                if(Mase[i][1]==trauk[j].nr):
                    print("Visa traukinio mase: ",Mase[i][0])
                    print("Traukinys: ",trauk[j])
                    print("----------------------------------------------------")                    
    else:
        print("Yveskite skaiciu 1 arba 2.")
        sorting()

def tikrintiInputui(sk):
    try:
        sk=int(sk)
    except ValueError as error:
        print('Negalima yvesti simbolio!\n')
        print('Error code: ' + repr(error) + '\n')
        writeJson()

#Lokomotyvo arba Vagono sukurimas
def writeJson():
#failas = input()
             ## '/mif/stud3/2014/tami1864/Python/3atsisk/'+ cia failas turi but
    with open(failas) as data_file:
        data=json.load(data_file)

    tipas = input("1. Lokomotyvas, 2. Vagonas, 3. Q - Gryzti y meniu , Parasykite pasirinkima: ")
    print("----------------------------------------------------")    

    if(tipas=="1"):
        tipas="lokomotyvas"

        mase = input("Yveskite mase: ")
        tikrintiInputui(mase)
        maxMase = input("Yveskite max mase: ")
        tikrintiInputui(maxMase)

        isvedimDuom = {'mase':int(mase),'maxMase':int(maxMase)}
        data[tipas].append(isvedimDuom)
#/mif/stud3/2014/tami1864/Python/3atsisk/
        with open(failas, 'w') as outfile:
            json.dump(data,outfile)
        print("----------------------------------------------------")
        print("Lokomatyvas sukurtas sekmingai!")
        print(data)

    elif(tipas=="2"):
        tipas="vagonas"

        mase=input("Yveskite mase: ")
        tikrintiInputui(mase)
        maxMase=input("Yveskite max mase: ")
        tikrintiInputui(maxMase)
        krovinioMase=input("Yveskite krovinio mase: ")
        tikrintiInputui(krovinioMase)
        nr=input("Yveskite krovinio numeri: ")
        tikrintiInputui(nr)

        isvedimDuom = {'mase':int(mase),'maxMase':int(maxMase),'krovinioMase':int(krovinioMase),'nr':int(nr)}
        data[tipas].append(isvedimDuom)
#/mif/stud3/2014/tami1864/Python/3atsisk/
        with open(failas, 'w') as outfile:
            json.dump(data,outfile)
        print("----------------------------------------------------")
        print("Vagonas sukurtas sekmingai!")
        print(data)
    elif(tipas == "q")or(tipas == "Q"):
        menu()
    else:
        print("!! Neteisingas pasirinkimas, privalo buti skaicius  !!")
        print("!! Galite pasirinkti 1(Lokomatyvas) arba 2(Vagonas) !!") 
        print("!! Spauskite Q, tam kad grysti y meniu              !!")       
        print("------------------------------------------------------")        
        writeJson()

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

#Menu tam, kad butu lengviau naviguoti
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
def tikrintiFailui(f):
    try:
        f = open(f)
    except FileNotFoundError as e:
        print("----------------------------------------------------")
        print("Failas "+ f +" nerastas!\n")
        print("Error code: " + repr(e))
        sys.exit(0)
 
failas = input("Yveskite failo pavadinima: ")
tikrintiFailui(failas)
menu()