
# Classe para o Objeto Ar-Condicionado

class Objeto:

	def __init__(self):
		self.nome: str = ""
		self.ligado = 0
		self.potencia: int = 0

	def aumentarPotencia(self):
		if(self.potencia < 100):
			self.potencia+=1

	def diminuirPotencia(self):
		if(self.potencia > 0):
			self.potencia-=1

	# Metódo para ligar o aparelho
	def turn_on(self) -> None:
		self.ligado = True

	# Metódo para desligar o aparelho
	def turn_off(self) -> None:
		self.desligado = False

	# Retorna o estado atual do aparelho
	def get_status(self):
		pass

class ArCondicionado(Objeto):

	nome = "Ar Condicionado"
	TEMPERATURAS = ( 16, 18, 20, 22, 24	)

	def aumentarPotencia(self):
		if(self.potencia < 4):
			Objeto.aumentarPotencia(self)

	def diminuirPotencia(self):
		if(self.potencia>0):
			Objeto.diminuirPotencia(self)

	def get_status(self):
		return bytearray([0, self.ligado, self.TEMPERATURAS[self.potencia]])

class Lampada(Objeto):
	nome = "Lâmpada"

	def get_status(self):
		return bytearray([1, self.ligado, self.potencia])
