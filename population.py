from enum import Enum


class DoençaValor(Enum):
    DOENCA_CARDIOVASCULAR = 40
    DIABETE = 35
    HIPERTENSAO = 30
    DOENCA_RESPIRATORIA_CRONICA = 25
    CANCER = 20
    INSUFICIENCIA_RENAL = 15
    IMUNO_DEFICIENCIA = 10
    SEM_COMORBIDADE = 5


MAPA_DE_DOENCA = {
    'doenca cardiovascular': DoençaValor.DOENCA_CARDIOVASCULAR.value,
    'diabete': DoençaValor.DIABETE.value,
    'hipertesao': DoençaValor.HIPERTENSAO.value,
    'doenca respiratoria cronica': DoençaValor.DOENCA_RESPIRATORIA_CRONICA.value,
    'cancer': DoençaValor.CANCER.value,
    'insuficiencia renal': DoençaValor.INSUFICIENCIA_RENAL.value,
    'imuno deficiencia': DoençaValor.IMUNO_DEFICIENCIA.value,
    '': DoençaValor.SEM_COMORBIDADE.value,
}


class Pessoa():
    def __init__(self, nome, cpf, idade, comorbidades):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.comorbidades = comorbidades
        self.perigo = 0 

    def calculo_perigo(self):
        if not self.comorbidades:
            return self.idade

        for doenca in self.comorbidades:
            self.perigo += MAPA_DE_DOENCA[doenca] * self.idade
        
        return self.perigo




