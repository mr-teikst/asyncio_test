import socket 
import time
import threading
ADDR = ("192.168.56.1",6666)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ADDR)



def handel (cli , addr):
	while True:
		msg = cli.recv(1024).decode("utf-8")
		if msg:
			print(msg)
		print("in procces")
		time.sleep(5)

		cli.send(bytes("massage arrived!","utf-8"))
		time.sleep(1)




def start():
	print("server listening ...")
	s.listen()
	#cli,addr =s.accept()
	#print (f"connection from {add} has been established!")
	while True:
		cli,addr =s.accept()
		thread = threading.Thread(target = handel,args=(cli,addr))
		thread.start()
		print (f"[ACTIVE CONNECTION] {threading.activeCount()-1}")


start()



"""cli.send(bytes(f"you're connect to {socket.gethostname()}","utf-8"))
while True:
	msg = s.recv(1024)

	if msg:
		msg = msg.decode("utf-8")
		print(msg)

	time.sleep(2)	
"""