import SimulacionMalla as sim
import LectorDeDatos as lector
import csv

ramosDict = lector.leer_ramos('Ramos Biomedica.csv')
malla = lector.leer_malla('MallaBiomedica.csv',ramosDict)

estudiante = sim.Estudiante(malla,ramosDict)
print("Semestres que se tardo: "+ str(estudiante.simular()))

n = 100000
frecuencias = []
desertores = []
total_desertores = 0

maxcreditos = float('inf')
maxvtr = 3

for i in range(n):
    estudiante = sim.Estudiante(malla,ramosDict,maxcreditos,maxvtr)
    aprobado, s = estudiante.simular()
    if aprobado:
        while s>=len(frecuencias):
            frecuencias.append(0)
        frecuencias[s]+=1
    else:
        while s>=len(desertores):
            desertores.append(0)
        desertores[s]+=1
        total_desertores += 1
    

print(frecuencias)
print("Desertores: " + str(desertores))
print("Total Desertores: "+str(total_desertores))

f = open('resultados.csv','w')
csvwriter = csv.writer(f,delimiter=';')
csvwriter.writerow(frecuencias)
csvwriter.writerow(desertores)
f.close()
