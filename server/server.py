import socket
import select

from srv_threads import ConnAccepterThread#, DataIncomeThread

##TODO: CONFIG FILE
SERVER_HOST_PORT = 8000

BFF_DATA_SIZE = 1024 #1K buffer

class SysSock():

	scklist = list()
	connlist = list()

	def start_threads(self):
		print 'creando threads'
		self.conn_accept = ConnAccepterThread(self)
		self.conn_accept.run()
		print 'threads creados'

	def __init__(self):
		self.__sck_config()
		self.__sck_listen()

	def __sck_config(self):
		#Create TCP/IP socket
		self.socket = socket.socket()

		self.host = socket.gethostname()
		self.port = SERVER_HOST_PORT
		self.socket.bind((self.host, self.port))

	def __sck_listen(self):
		self.socket.listen(5)


class Conn():
	def __init__(self, sck, addr):
		self.sck = sck
		self.addr = addr 

	def __str__(self):
		return self.addr[0]

	def get_sck(self):
		return self.sck

	def data_recv(self):
		return self.get_sck().recv(BFF_DATA_SIZE)

def __main():
	print 'main'
	sys_sck = SysSock()
	print 'sys sock creada'
	sys_sck.start_threads()

	print 'while true'
	while True:
		pass

__main()