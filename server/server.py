import socket

s = socket.socket()
host = socket.gethostname()
port = 8888
s.bind((host, port))

s.listen(5)

while True:
	c, addr = s.accept()
	print 'Accepting connection from', addr
	c.send('Welcome to Paskeil\'s server')
	c.close()