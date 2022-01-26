#!/bin/python3

import sys
from datetime import datetime
import socket

#getting target
if len(sys.argv) == 2: 		#2 as python3 pscan.py <IP> ; so two arguments
	target = socket.gethostbyname(sys.argv[1]) 	#translate hostname to IP
else:
	print("""invalid syntax. 
Syntax: ./pscan.py <IP>""")

#pretty banner
print("-" * 50)
print("Scanning target:" + target)  #verifying target
print("Time started: " + str(datetime.now())) 	#converting time now to string as cannot contcatenate different types in python
print("-"*50) 

try:
	for port in range(1,500):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defining a socket variable
		socket.setdefaulttimeout(1)	#default timeout set to 1 sec
		result = s.connect_ex((target, port)) #returns 1 if error occurs, unless 0
#		print("checking port {}".format(port))
		if result == 0:
			print("Port {} is open.".format(port))
		s.close()	#closing connection

except KeyboardInterrupt:
	print("Exiting program")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
