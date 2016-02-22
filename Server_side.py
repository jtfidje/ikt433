#-----------------------------------------------------#
#				   Server_side.py                     #
#-----------------------------------------------------#

import sys
import time
import socket					# Socket module
import request
import threading

class cThread (threading.Thread):
	def __init__(self, c, addr):
		threading.Thread.__init__(self)
		self.c = c
		self.addr = addr

	def run(self):
		while True:
			active_connection(self.c, self.addr)

def active_connection(c, addr):
	while True:
		client_message = c.recv(buff).split(' ')
		
		if client_message:		
			print(">"+ ''.join(client_message))

			if client_message[0] == "logout":
				s.listen(5)						# Sets up and start TCP listener
				c, addr = s.accept()
				print 'Connected: ', addr
				
			elif client_message[0] == "help":
				c.send('Commands>> Type `command`, `space` and input \n >>\n help\n logout\n getphone `input = ID`\n getmail1 `input = ID`\n getmail2 `input = First and last name`\n findall `input = Department ID`\n')
			
			elif client_message[0] == "getphone":
				parameters = client_message[1]
				output = str(request.request_phone(parameters))
				c.send(output)
			
			elif client_message[0] == "getmail1":
				parameters = client_message[1]
				output = str(request.request_email_by_ID(parameters))
				c.sendall(output)
				
			elif client_message[0] == "getmail2":
				parameters1 = client_message[1]
				parameters2 = client_message[2]
				output = str(request.request_email_by_name(parameters1, parameters2))
				c.send(output)	
				
			elif client_message[0] == "findall":
				parameters = client_message[1]
				output = request.Find_all_emails_by_dep(parameters)
				output = '\n>'.join(output)
				c.send(output)
			else:
				c.send("Command not defined")
			
			client_message = None

s = socket.socket()				# Create a socket object
host = socket.gethostname()		# Get local machine name
port = 12345					# Reserve a port
buff = 4096						# Buffer size
s.bind((host, port))			# Bind to the port

threads = []

while True:
	s.listen(5)						# Sets up and start TCP listener
	
	c, addr = s.accept()			# Establish connection
	
	try:
		thread = cThread(c, addr)	# Create new thread
		thread.start()				# Start thread
		threads.append(thread)		# If thread started, append to list of threads
		
		# Print connection message
		print 'Connected: ', addr
		c.send('You are now connected to the server >>  ')
	except:
		print "Error: Couldn't establish new connection in thread"

	time.sleep(0.5)
	
for thread in threads:		# Exit all threads
	thread.exit()

c.close()					# Close the connection