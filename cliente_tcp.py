#!/usr/bin/env python3

import socket
from objetos import ArCondicionado,Lampada

class Client:

	message = bytearray(4)
	OBJECT_TYPE = (
		'Ar Condicionado',
		'Lampada',
	)
	OBJECT_STATUS = (
		'Desligado',
		'Ligado',
	)

	def traduzir_status(self, reply):
		if reply[0] == 3:
			return "---"*8
		return "O objeto {0} está: {1}. A potencia é = {2}.".format(self.OBJECT_TYPE[reply[0]], self.OBJECT_STATUS[reply[1]], reply[2])

	def __init__(self):
		self.ar = ArCondicionado()
		self.lampada = Lampada()
		self.entrada = 1
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(('localhost', 6070))
		print('Cliente atríbuido socket: ', sock.getsockname())

		continua = True
		while continua:

			# TODO Perguntar Opcao GET ou SET
			self.get_entrada(1)

			if (self.entrada == 0):
				continua = False
				break

			if(self.message[0] == 1): # se escolher alterar configuração
				self.set_objeto(2) 
				if (self.entrada==0): # se escolher 0, encerra a programação
					continua = False
					break
				self.set_escolha(3)
				if (self.message[2]==0): # se escolher On/Off
					self.set_ligar(4)
					sock.send(bytes(self.message))
				else: # se escolher aumentar/reduzir
					self.set_potencia(4)
					sock.send(bytes(self.message))
			else:
				sock.send(bytes(self.message))

			reply = sock.recv(4)
			print('Resposta do Servidor:', self.traduzir_status(reply))
			reply = sock.recv(4)
			print('Resposta do Servidor:', self.traduzir_status(reply))
		sock.close()

	def get_entrada(self, opcao):
		print("1 - Ver o estado dos objetos")
		print("2 - Alterar o estado dos objetos")
		print("Digite 0 e tecle ENTER a qualquer momento para sair : ")
		print("Digite o número da opção e tecle ENTER: ")
		self.entrada = int(input())
		if self.entrada > 0:
			self.message[opcao-1] = self.entrada-1

	def set_objeto(self, opcao):
		print("1 - Ar Condicionado")
		print("2 - Lampada")
		print("Digite o número da opção e tecle ENTER: ")
		self.entrada = int(input())
		if self.entrada > 0:
			self.message[opcao-1] = self.entrada-1

	def set_escolha(self, opcao):
		print("1 - On/Off")
		print("2 - Aumentar/Reduzir")
		print("Digite o número da opção e tecle ENTER: ")
		self.entrada = int(input())
		if self.entrada > 0:
			self.message[opcao-1] = self.entrada-1

	def set_ligar(self, opcao):
		print("1 - Desligar")
		print("2 - Ligar")
		print("Digite o número da opção e tecle ENTER: ")
		self.entrada = int(input())
		if self.entrada > 0:
			self.message[opcao-1] = self.entrada-1

	def set_potencia(self, opcao):
		print("1 - Reduzir")
		print("2 - Aumentar")
		print("Digite o número da opção e tecle ENTER: ")
		self.entrada = int(input())
		if self.entrada > 0:
			self.message[opcao-1] = self.entrada-1




if __name__ == '__main__':
	Client()
