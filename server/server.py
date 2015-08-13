import socket
import thread

class SysSock():

	userlist = list()

	def __init__(self):
		self.__sck_config()
		self.__sck_listen()

	def __sck_config(self):
		self.socket = socket.socket()
		self.host = socket.gethostname()
		self.port = 8888
		self.socket.bind((self.host, self.port))

	def __sck_listen(self):
		self.socket.listen(5)

	def conn_accept(self):
		c, addr = self.socket.accept()
		c.send('Welcome to Paskeil\'s server')
		c.close()
		return addr

	def thread_conn_accept(self, thread_name):
		while True:
			addr = self.conn_accept()
			print thread_name, ": Accepting connection from ", addr


def __main():
	sys_sck = SysSock()
	thread.start_new_thread(sys_sck.thread_conn_accept, ("Thread-Accepter",) )

	while True:
		pass

__main()