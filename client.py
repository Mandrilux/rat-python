import socket

host='lab.baptisteheraud.com'
port=4242

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True :
    command = input("Enter your command :\n")
    s.send(command.encode())
    print("Command send")
    print("en attente de reception")
    data = s.recv(15000)
    print(data.decode())

