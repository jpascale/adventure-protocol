import thread

class ConnAccepterThread():
	thread_name = 'Thread-Accepter'

	def __init__(self, sys_sck):
		self.sys_sck = sys_sck

	def conn_accept(self):
		sck, addr = self.sys_sck.socket.accept()
		sck.send('Welcome to Paskeil\'s server')
		#sck.close()
		return addr

	def thread_conn_accept(self):
		while True:
			addr = self.conn_accept()
			print self.thread_name, '> Incoming connection from ', addr

	def run(self):
		thread.start_new_thread(self.thread_conn_accept, () )

'''
class DataIncomeThread():
	thread_name = 'Thread-DataIncome'

	def __init__(self, sys_sck):
		self.sys_sck = sys_sck

	def thread_conn_data_receive(self):
		potencial_readers = self.sys_sck.scklist
		potencial_writers = list()
		in_error = list()

		while True:
			ready_to_read, ready_to_write, in_error = \
               	select.select(
                	potential_readers,
                	potential_writers,
                	potential_errs,
                	timeout)

            for sck in ready_to_read:
            	print thread_name, '> ', sck.

	def run(self):
		thread.start_new_thread(self.thread_conn_data_receive(), ())
'''
