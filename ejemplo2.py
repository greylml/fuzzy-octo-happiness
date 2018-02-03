class RobotUtopian:
	"""Segundo ejemplo para steemit
	haciendo uso del metodo __init__"""
	def __init__(self, categoria):
		self.categoria = categoria

	def saludar(self,saludo):
		print(saludo)

	def upvote(self,votame):
		print(votame)

	def canto(self,cantar):
		print(cantar)

utopiaman = RobotUtopian("Reploid")
robotboy = RobotUtopian("Maverick")

print(utopiaman.categoria)

utopiaman.saludar("Beep, saludo humano, soy el robot utopiaman")
robotboy.saludar("Beep, saludo humano, yo soy robotboy")
utopiaman.upvote("no olvides votarnos y compartir")