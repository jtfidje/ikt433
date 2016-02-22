#-----------------------------------------------------#
#				   Client_side.py                     #
#-----------------------------------------------------#

import socket
import sys

s = socket.socket()				# Create a socket object
host = 'localhost'				# Get local machine name
port = 60000					# Reserve a port
s.connect((host, port))			# Connecting
buff = 4096						# Buffer size

user = raw_input('Please enter your email:')

s.send(user)

answ = s.recv(buff)

if answ == 'duplicate':
	print 'User already logged in. Exiting...'
	sys.exit(1)
	s.close()
if answ == 'invalid':
	print 'Username don\'t exist. Exiting...'
	sys.exit(1)
	s.close()

print "\n"
print answ + "\n"
print "|------------------------------|"
print "|            Client:           |"
print "|     Type 'help' for help     |"
print "|------------------------------|" + "\n"

while True:
	# Send input
	cmd = raw_input('Input command:\n').strip()
	
	if cmd == "logout":
		s.send(cmd)
		print 'Bye!'
		s.close()
		sys.exit(0)
	else:
		if not bool(cmd.strip()):
			continue
		s.send(cmd)
		
		# Wait for server response
		line = s.recv(buff)

		# Dont print empty shit
		if not bool(line.strip()):
			continue
		
		#Print response
		print(">"+line)