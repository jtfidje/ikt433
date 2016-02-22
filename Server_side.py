#-----------------------------------------------------#
#				   Server_side.py                     #
#-----------------------------------------------------#

import sys
import time
import socket
import request
import threading

threads = {}

'''
Class used to establish new connections on separate threads
'''
class cThread (threading.Thread):
	def __init__(self, c, addr, user):
		threading.Thread.__init__(self)
		self.user = user
		self.c = c
		self.addr = addr

	def run(self):
		active_connection(self.c, self.addr, self.user)

'''
Function to handle active connections and client messages
'''
def active_connection(c, addr, user):
	while True:
		client_message = c.recv(buff).split(' ')
		
		if client_message:		
			print(">"+ ''.join(client_message))

			if client_message[0] == "logout":
				print user, "logged out. Closing connection."
				c.close()
				del threads[user]
				break
				
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

			elif client_message[0] == 'getonline':
				output = request.get_online(threads)
				c.send(output)

			else:
				c.send("Command not defined")
			
			client_message = None

try:
	s = socket.socket()					# Create a socket object
	host = 'localhost'					# Get local machine name
	port = 60000						# Reserve a port
	buff = 4096							# Buffer size
	s.bind((host, port))				# Bind to the port

	while True:
		s.listen(5)							# Sets up and start TCP listener
		c, addr = s.accept()				# Establish connection
		print 'Incoming connection...'
		user = c.recv(buff)					# Get user
		if not request.login(user):
			print 'Invalid username... Closing connection'
			c.send('invalid')
			c.close()
			continue
		try:
			if user not in threads:
				thread = cThread(c, addr, user)	# Create new thread
				thread.start()					# Start thread
				threads[user] = thread			# If thread started, append to list of threads
				
				# Print connection message
				print user, 'connected from: ', addr
				c.send('Welcome ' + user + '\nYou are now connected to the server!  ')
			else:
				print 'Duplicate login... Closing connection.'
				c.send('duplicate')
				c.close()
		except:
			print "Error: Couldn't establish new connection in thread"

		time.sleep(0.5)
except KeyboardInterrupt:
	print ''
	if threads:
		try:
			print 'Closing sockets...'
			for thread in threads:
				thread.c.close()
		except:
			pass
	s.close()
	print 'Exiting...'
	sys.exit(0)