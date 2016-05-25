import json
import sys

def readWriteJson():
    #failas = input()
              # '/mif/stud3/2014/tami1864/Python/3atsisk/'+ cia failas turi but
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
readWriteJson()