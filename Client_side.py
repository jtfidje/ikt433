#-----------------------------------------------------#
#				   Client_side.py                     #
#-----------------------------------------------------#

import socket					# Socket module
import sys

s = socket.socket()				# Create a socket object
host = socket.gethostname()		# Get local machine name
port = 12345					# Reserve a port
s.connect((host, port))			# Connecting
buff = 4096						# Buffer size
print "\n"
print s.recv(buff) + "\n"
print "|------------------------------|"
print "|------------Client:-----------|"
print "|-----Type-'help'-for-help-----|"
print "|------------------------------|" + "\n"

while True:
	# Send input
	cmd = raw_input('Input command:\n').strip()
	if cmd == "logout":
		s.send(cmd)
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