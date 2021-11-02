#!/usr/bin/env python3

import socket

def client(host='localhost', port=1060):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))
	print('Client has been assigned socket name: ', sock.getsockname())
	msg = input("END para sair;")
	while(msg != "END"):
		sock.send(str.encode(msg))
		reply = sock.recv(1)
		print('The server said,', repr(reply))
		msg = input("END para sair;")

	sock.close()

if __name__ == '__main__':
	client()