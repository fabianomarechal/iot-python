
# Classe para o Objeto Ar-Condicionado

class Objeto:
	def __init__(self):
		self.nome: str = ""
		self.ligado: bool = False
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
	def __str__(self) -> str:
		return "O objeto {0} está: {1}. A potencia é = {2}.".format(self.nome, 'Ligado' if self.ligado else 'Desligado', self.potencia)

class ArCondicionado(Objeto):

	nome = "Ar Condicionado"
	TEMPERATURAS = (
		{0, '16ºC'},
		{1, '18ºC'},
		{2, '20ºC'},
		{3, '22ºC'},
		{4, '24ºC'},
	)

	def aumentarTemperatura(self):
		if(self.potencia < 4):
			self.aumentarPotencia()

	def diminuirTemperatura(self):
		if(self.potencia>0):
			self.diminuirPotencia()

class Lampada(Objeto):
	nome = "Lâmpada"
