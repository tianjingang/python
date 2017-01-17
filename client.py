#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-



#导入socket模块
import socket
#创建socket对象
s = socket.socket()
#获取本地主机名
host = '127.0.0.1'
#设置端口
port=12345

s.connect((host, port))
print s.recv(1024)
s.close()