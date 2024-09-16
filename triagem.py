import random
from paciente import Paciente

class Triagem:
	nomes_triagem = ["Fabricio", "Giovanna", "Galamundna", "Mavven", "Izabela"]
	paciente_nome = ["Leonardo", "Domartelo", "Da20", "LilRafa", "Dilma", "Aria"]
	prioridade = ["vermelho", "laranja", "verde", "azul"]
	
	def __init__(self):
		self.nome = random.choice(Triagem.nomes_triagem)
		print(f"Olá, meu nome é {self.nome} sou a T-R-I-A-G-E-M")
		print(f"[{self.nome}]: Me diga seus dados biologicos e o que está sentindo!")
		self.a = Paciente()

	def dar_pulseira(self):
		print(f"[{self.nome}]: Pronto! Toma essa pulseira que já vão te chamar :)")
		pri = random.randint(0 , 3)
		pri0 = Triagem.prioridade[pri]
		return pri0


	def triagem( self ):
		return self.a.dados()
		
		