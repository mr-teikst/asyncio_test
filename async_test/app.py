import kivy
import socket
from kivy.app import App
from kivy.lang import Builder
import asyncio
from kivy.core.window import Window


class Icli:
	async def start_cli(self):
		ADDR=("192.168.56.1",6666)
		self.s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.connect(ADDR)
		#print(self.s.recv(1024).decode("utf-8"))


	async def send(self,data):
		self.s.send(bytes(data,"utf-8"))
		msg_come = False
		while not(msg_come):
			msg_come =self.s.recv(1024).decode("utf-8")
		print (msg_come)



kv = Builder.load_file('app.kv')

class MyApp(App):
	Window.size = (200,200)

	def build(self):
		self.icli= Icli()
		#cli_run = asyncio.create_task(self.icli.start_cli())
		asyncio.run(self.icli.start_cli())
		return kv


		

if __name__=="__main__":
		app = MyApp()
		app.run()





