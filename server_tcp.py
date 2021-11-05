#!/usr/bin/env python3

import socket
from objetos import ArCondicionado,Lampada


class Server:

	message = bytearray(4)

	def send_status(self, sock):
		if self.message[0] == 0: # se GET_STATUS recebido
			sock.send(bytes(self.ar.get_status()))
			sock.send(bytes(self.lampada.get_status()))
		else:
			if self.message[1]==0:
				if self.message[2]==0: # On/OFF
					self.ar.turn_off() if self.message[3]==0 else self.ar.turn_on() # On/Off
				else:
					self.ar.diminuirPotencia() if self.message[3]==0 else self.ar.aumentarPotencia() # Aumentar/Reduzir
				sock.send(bytes(self.ar.get_status()))
				sock.send(bytes([3,0,0]))
			else:
				if self.message[2]==0: # On/OFF
					self.lampada.turn_off() if self.message[3]==0 else self.lampada.turn_on() # On/Off
				else:
					self.lampada.diminuirPotencia() if self.message[3]==0 else self.lampada.aumentarPotencia() # Aumentar/Reduzir
				sock.send(bytes(self.lampada.get_status()))
				sock.send(bytes([3,0,0]))

	def __init__(self):
		self.ar = ArCondicionado()
		self.lampada = Lampada()


		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(('localhost', 6070))
		sock.listen(4)
		print('Escutando na porta: ', sock.getsockname())

		sc, sockname = sock.accept()
		print('Aceitamos conexão de: ', sockname)
		print('Nome do Socket: ', sc.getsockname())
		print('Peer do Socket: ', sc.getpeername())
		while True:
			self.message = sc.recv(4)
			print('Recebendo 8 bits de mensagem: ', repr(self.message))
			self.send_status(sc)
			# sc.sendall(b'0')
		sc.close()
		print('Resposta enviada, conexão fechada')

if __name__ == '__main__':
	Server()