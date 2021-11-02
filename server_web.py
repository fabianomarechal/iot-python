#!/usr/bin/env python3

import argparse, socket

def recvall(sock, length):
	data = b''
	while len(data) < length:
		more = sock.recv(length - len(data))
		if not more:
			raise EOFError('was expecting %d bytes but only received %d bytes before the socket closed' % (length, len(data)))
		data += more
	return data

def server(interface, port):
	sock = socket.socket()
	sock.bind((interface, port))
	sock.listen(5)
	print('Escutando na porta: ', sock.getsockname())
	while True:
		sc, sockname = sock.accept()
		print('Aceitamos conexão de: ', sockname)
		print('Nome do Socket: ', sc.getsockname())
		print('Peer do Socket: ', sc.getpeername())
		message = sc.recv(1000)
		print('Recebendo 16 octetos de mensagem: ', message)
		sc.send(b'HTTP/1.1 200 OK\n')
		sc.send(b'Content-Type: text/html\n')
		sc.send(b"""
				<!DOCTYPE html>
				<html>
				<head>
					<meta charset="utf-8">
					<title>IoT com Python</title>
					<style type="text/css">
						body {
							background: #ccc;
						}
						.lampada {
							background-image: url("https://freesvg.org/img/1434619451.png");
						    background-position: left;
						    background-size: cover;
						    width: 150px;
						    height: 313px;
						    overflow: hidden;
						}
						.lampada[disabled] {
							background-image: url(https://freesvg.org/img/1434619451.png);
						    background-position: right;
						    background-size: cover;
						    width: 150px;
						    height: 313px;
						    overflow: hidden;
						}
					</style>
				</head>
					<body>
						<div class="lampada" disabled=false> </div>
						<!-- <div id="lampada2"> </div> -->
						<!-- <img src="lampada.svg" width="300px"> -->

					</body>
				</html>
			""")
		# sc.sendall(b'Farewell, client')
		sc.close()
		print(' Resposta enviada, conexão fechada')

def client(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	print('Client has been assigned socket name: ', sock.getsockname())
	sock.sendall(b'hi there, server')
	reply = recvall(sock, 16)
	print('The server said,', repr(reply))
	sock.close()

if __name__ == '__main__':
	choices = {'client': client, 'server': server}
	parser = argparse.ArgumentParser(description='Send and Receive over TCP')
	parser.add_argument('role', choices=choices, help='which role to play')
	parser.add_argument('host', help='interface the server listens at hosts the client sends to')
	parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port (default 1060)')
	args = parser.parse_args()
	function = choices[args.role]
	function(args.host, args.p)