import csv
import SimulacionMalla as sim

def leer_ramos(archivo):
    f = open(archivo,'r')
    ramos_list = list(csv.reader(f,delimiter=';'))
    print(ramos_list[1:])
    ramosDict = dict()

    for nombre ,sigla, prob, prereq in ramos_list[1:]:
        #sigla, prob, prereq = csv_ramos[i]
        print(sigla +" "+ prob +" "+ prereq)
        prob = float(prob)
        prereq = prereq.split()
        ramo = sim.Ramo(sigla, prob, prereq)
        ramosDict[ramo.sigla] = ramo
    
    f.close()
    return ramosDict
    
def leer_malla(archivo, ramosDict):
    f = open(archivo,'r')
    csv_malla = csv.reader(f, delimiter=';')
    malla = []

    for semestre in csv_malla:
        ramos = set()
        for sigla in semestre[1:]:
            ramos.add(ramosDict[sigla])
        malla.append(ramos)
        
    f.close()
    return malla