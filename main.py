from objetos import ArCondicionado, Lampada

if __name__ == '__main__':
	ar = ArCondicionado()
	print("Verificando Ar-Condicionado")
	print(ar)
	print("Ligando Ar-Condicionado")
	ar.turn_on()
	print("Verificando Ar-Condicionado")
	print(ar)

	l = Lampada()
	print(l)
	