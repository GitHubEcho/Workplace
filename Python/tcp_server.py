#!usr/bin/python
#coding:utf-8

import socket

HOST = '127.0.0.1'
PORT = 8001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()
print("The Server is listening %s:%s"%(HOST,PORT))

while True:#无限循环等待用户连接
    conn,addr = s.accept()
    print("connected by ",addr)

    while True:#无限循环接收用户消息
        data = conn.recv(1024)
        print("client>",data.decode())
        msg = 'Server have received your msg'
        conn.send(msg.encode())

    conn.close()

