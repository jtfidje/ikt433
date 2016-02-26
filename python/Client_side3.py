#-----------------------------------------------------#
#				   Client_side3.py                     #
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
print "|-------Get_phone_by_ID--------|"
print "|------------------------------|\n"

while True:
	# Send input
	input = raw_input('Type ID:\n')
	cmd = ("getphone" + " " + input).strip()
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