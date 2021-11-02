#!/usr/bin/env python3

import socket


def server(interface, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((interface, port))
	sock.listen(1)
	print('Escutando na porta: ', sock.getsockname())
	while True:
		sc, sockname = sock.accept()
		print('Aceitamos conexão de: ', sockname)
		print('Nome do Socket: ', sc.getsockname())
		print('Peer do Socket: ', sc.getpeername())
		message = sc.recv(1)
		print('Recebendo 8 bits de mensagem: ', repr(message))
		sc.sendall(b'0')
		sc.close()
		print(' Resposta enviada, conexão fechada')

if __name__ == '__main__':
	server('localhost', 1060)