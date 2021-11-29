import socket

host='lab.baptisteheraud.com'
port=4242

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True :
    command = input("Enter your command :\n")
    if command.upper() == "exit".upper():
        break
    print("[+] send " + command)
    s.send(command.encode())
    data = s.recv(15000)
    print(data.decode())
s.close()