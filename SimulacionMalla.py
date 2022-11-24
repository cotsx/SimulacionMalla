import random

class Ramo:
    def __init__(self, sigla, prob, prereq, creditos):
        self.sigla = sigla
        self.prob = prob
        self.prereq = prereq
        self.creditos = creditos
    def cumple_prereq(self, estudiante):
        for prereqsigla in self.prereq:
            if  not estudiante.info_ramos[prereqsigla].aprobado:
                return False
        return True
    def pasa(self, estudiante):
        vtr = estudiante.info_ramos[self.sigla].vtr
        vtr = min(vtr,len(self.prob))
        return random.random() <= self.prob[vtr-1]

class Estudiante:
    def __init__(self, malla, ramosDict, maxcreditos = float('inf'), maxvtr=float('inf')):
        self.malla = malla
        self.ramosDict = ramosDict
        self.semestre = 0
        self.info_ramos = {}
        self.por_aprobar = set()
        self.maxcreditos = maxcreditos
        self.maxvtr=maxvtr
        for sigla in ramosDict:
            self.info_ramos[sigla] = InfoRE()
        for s in malla:
            for ramo in s:
                self.por_aprobar.add(ramo)
    def elegir_ramos(self):
        creditos = 0
        ramos_a_tomar = set()
        for i in range(min(self.semestre,len(self.malla))):
            for ramo in self.malla[i]:
                if not self.info_ramos[ramo.sigla].aprobado:
                    if ramo.cumple_prereq(self):
                        if creditos + ramo.creditos <= self.maxcreditos:
                            ramos_a_tomar.add(ramo)
                            creditos += ramo.creditos
        return ramos_a_tomar
    def simular(self):
        termino=False
        while self.por_aprobar: #mientras el por_aprobar no esté vacio
            self.semestre += 1
            #print("semestre: "+ str(self.semestre))
            ramos_a_tomar = self.elegir_ramos();
            for ramo in ramos_a_tomar:
                #print("El estudiante toma "+ramo.sigla)
                self.info_ramos[ramo.sigla].vtr += 1
                if (ramo.pasa(self)):
                    #print("El estudiante aprueba")
                    self.info_ramos[ramo.sigla].aprobado = True
                    self.por_aprobar.remove(ramo)
                else:
                    #print("El estudiante reprueba")
                    if self.info_ramos[ramo.sigla].vtr>=self.maxvtr:
                        return -1
        return self.semestre

class InfoRE:
    def __init__(self, vtr=0, aprobado=False):
        self.vtr = vtr
        self.aprobado = aprobado

