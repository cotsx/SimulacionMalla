import random

class Ramo:
    def __init__(self, sigla, prob, prereq):
        self.sigla = sigla
        self.prob = prob
        self.prereq = prereq
    def cumple_prereq(self, estudiante):
        for prereqsigla in self.prereq:
            if  not estudiante.ramosDict[prereqsigla] in estudiante.aprobados:
                return False
        return True
    def pasa(self, estudiante):
        return random.random() <= self.prob

class Estudiante:
    def __init__(self, malla, ramosDict):
        self.malla = malla
        self.ramosDict = ramosDict
        self.semestre = 0
        self.aprobados = set()
        self.por_aprobar = set()
        for s in malla:
            for ramo in s:
                self.por_aprobar.add(ramo)
    def elegir_ramos(self):
        ramos_a_tomar = set()
        for i in range(min(self.semestre,len(self.malla))):
            for ramo in self.malla[i]:
                if ramo not in self.aprobados:
                    if ramo.cumple_prereq(self):
                        ramos_a_tomar.add(ramo)
        return ramos_a_tomar
    def simular(self):
        termino=False
        while self.por_aprobar: #mientras el por_aprobar no esté vacio
            self.semestre += 1
            #print("semestre: "+ str(self.semestre))
            ramos_a_tomar = self.elegir_ramos();
            for ramo in ramos_a_tomar:
                #print("El estudiante toma "+ramo.sigla)
                if (ramo.pasa(self)):
                    #print("El estudiante aprueba")
                    self.aprobados.add(ramo)
                    self.por_aprobar.remove(ramo)
                else:
                    #print("El estudiante reprueba")
                    pass
        return self.semestre



##ramosDict = dict()
##
##ramo0 = Ramo("RAM100",0.8,set())
##ramo1 = Ramo("RAM101",0.7,{"RAM100"})
##ramo2 = Ramo("RAM102",0.6,{"RAM101"})
##ramo3 = Ramo("RAM103",0.8,{"RAM102"})
##
##ramosDict[ramo0.sigla] = ramo0
##ramosDict[ramo1.sigla] = ramo1
##ramosDict[ramo2.sigla] = ramo2
##ramosDict[ramo3.sigla] = ramo3
##
##
##
##malla = [{ramo0},{ramo1},{ramo2},{ramo3}]
##
##estudiante = Estudiante(malla, ramosDict)
##print(estudiante.simular())
