
# Classe para o Objeto Ar-Condicionado

class Objeto:
	nome: str = ""
	ligado: bool = False
	potencia: int = 0

	# Metódo para ligar o aparelho
	def turn_on(self) -> None:
		self.ligado = True

	# Metódo para desligar o aparelho
	def turn_off(self) -> None:
		self.desligado = False

	# Retorna o estado atual do aparelho
	def __str__(self) -> str:
		return "O objeto {0} está: {1}".format(self.nome, 'Ligado' if self.ligado else 'Desligado')

class ArCondicionado(Objeto):

	nome = "Ar Condicionado"

class Lampada(Objeto):
	nome = "Lâmpada"
