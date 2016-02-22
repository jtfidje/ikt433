#-----------------------------------------------------#
#				  Client_side2.py                     #
#-----------------------------------------------------#

import socket					
import sys

s = socket.socket()				
host = socket.gethostname()		
port = 12345					
s.connect((host, port))			
print s.recv(4096) + "\n"

while True:
	# Send input
	input = raw_input('Type Name:\n')
	cmd = ("getmail2" + " " + input).strip()
	s.send(cmd)
	line = s.recv(4096)
	print(">"+line)