import SimulacionMalla as sim
import LectorDeDatos as lector
import csv

ramosDict = lector.leer_ramos('RamosDePrueba1.csv')
malla = lector.leer_malla('MallaDePrueba1.csv',ramosDict)

estudiante = sim.Estudiante(malla,ramosDict)
print("Semestres que se tardo: "+ str(estudiante.simular()))

n = 100000
frecuencias = []

for i in range(n):
    estudiante = sim.Estudiante(malla,ramosDict)
    s = estudiante.simular()
    while s>=len(frecuencias):
        frecuencias.append(0)
    frecuencias[s]+=1

print(frecuencias)

f = open('resultados.csv','w')
csvwriter = csv.writer(f,delimiter=';')
csvwriter.writerow(frecuencias)
f.close()
