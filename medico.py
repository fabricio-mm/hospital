from abc import ABC, abstractmethod
import random

class Medico:
    gripe = ['Tosse persistente', 'Febre alta', 'Dor de garganta', 'Congestão nasal', 'Dores musculares']
    diarreia = ["Diarreia frequente, Desidratação, Dor abdominal, Náuseas, Vômitos"]
    aids = ["Fadiga extrema", "Perda de peso","Febre recorrente", "Infecções oportunistas", "Suores noturnos" ]
    nomes = ["Arlindo", "Moura", "Rafaela", "Bianca", "Fernanda", "Sabrina"]
    dados = []
    def __init__(self):
        self.crm = random.randint(00000000,9999999)
        self.nome = random.choice(Medico.nomes)
        Medico.dados.append(self.crm)
        Medico.dados.append(self.nome)

    @abstractmethod
    def diagnostico( self, prioridade, sintomas):
            dor = [ ]
            for sintoma in sintomas:
                dor.append(sintoma)
            if dor == Medico.gripe:
                return "Gripe"
            elif dor == Medico.aids:
                return "Aids"
            elif dor == Medico.diarreia:
                return "Diarreia"
            else:
                return "Doença desconhecida para esse Hospital"
            

    @abstractmethod    
    def receita( self, doenca ):
        if doenca == "Diarreia":
            print(f"[{self.nome}]: Você tem {doenca}. Será necessário tomar Loperamida, 2 vezes por dia por 3 dias")
        elif doenca == "Aids":
            print(f"[{self.nome}]: Infelizmente você tem {doenca}. O tratamento com antirretrovirais é essencial para controlar o HIV/AIDS")
        elif doenca == "Gripe":
            print(f"[{self.nome}]: Você tem {doenca}. Será necessário tomar Loratadina, 2 vezes por dia por 5 dias")

class Residente(Medico):
    def __init__(self, prioridade):
        self.prioridade = prioridade
        
    def diagnostico( self ):
        doencas_listas = ["Gripe", "Diarreia", "Aids"]
        rando = random.choice(doencas_listas)
        if rando == "Gripe":
            return "Gripe"
        elif rando == "Aids":
            return "Aids"
        elif rando == "Diarreia":
            return "Diarreia"
        else:
            return "Doença desconhecida para esse Hospital"

    def receita(self, doenca):
        if doenca == "Diarreia":
            print(f"[Residente]: Como você está fedendo, deve ser {doenca}. Será necessário tomar Loperamida, 2 vezes por dia por 3 dias")
        elif doenca == "Aids":
            print(f"[Residente]: Então meu nobre, você tem {doenca}!! Desculpe, infelizmente. O tratamento com antirretrovirais é essencial para controlar o HIV/AIDS")
        elif doenca == "Gripe":
            print(f"[Residente]: Eu acho que vc tem {doenca}. Será necessário tomar Loratadina, 2 vezes por dia por 5 dias")