import random

class Paciente:
	d1 = ['Tosse persistente', 'Febre alta', 'Dor de garganta', 'Congestão nasal', 'Dores musculares']
	d2 = ["Fadiga extrema", "Perda de peso","Febre recorrente", "Infecções oportunistas", "Suores noturnos"]
	d3 = ["Diarreia frequente, Desidratação, Dor abdominal, Náuseas, Vômitos"]
	paciente_nome = ["Leonardo", "Domartelo", "Da20", "LilRafa", "Dilma", "Aria"]
	
	def __init__(self):
		self.nome = random.choice(Paciente.paciente_nome)
		self.idade = random.randint(12,80)
		self.peso = random.randint(45, 113)
		self.sintomas = random.choice([Paciente.d1, Paciente.d2, Paciente.d3])

	def dados( self ):
		print(f"[{self.nome}]: Meu nome é {self.nome}")
		print(f"[{self.nome}]: Eu tenho {self.idade} anos")
		print(f"[{self.nome}]: Peso {self.peso}Kg")
		print(f"[{self.nome}]: Estou sentindo {self.sintomas}")
		return self.sintomas
