#!usr/bin/python
# coding:utf-8

import socket

HOST = '127.0.0.1'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))

while True:
    msg = input("please you msg:")
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())
