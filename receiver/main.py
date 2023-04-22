import socket
import requests

UDP_IP = "127.0.0.1"
UDP_PORT = 1000

sock = socket.socket(socket.AF_INET, # Internet
					 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

changed = " "

def req():
	if item == "Light1":
		url = 'http://127.0.0.1:3000/l1'
		r = requests.post(url)
		print(r.json())
		print("Light1")

	elif item == "Light2":
		url = 'http://127.0.0.1:3000/l2'
		r = requests.post(url)
		print(r.json())
		print("Light2")
	elif item == "Door":
		url = 'http://127.0.0.1:3000/d'
		r = requests.post(url)
		print(r.json())
		print("Door")
	elif item == "Blind":
		url = 'http://127.0.0.1:3000/b'
		r = requests.post(url)
		print(r.json())
		print("blind")
	else:
		pass
	

while True:
	data, addr = sock.recvfrom(10000)
	parse = ("%s" % data)
	n = parse.split("\\x06")
	parse = n[2]
	n = parse.split("\\t")
	item = n[0]
	req()


	
	


