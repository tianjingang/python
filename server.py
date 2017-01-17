#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-




import socket   #引入socket模块


#创建socket对象
s = socket.socket()
#获取本地主机名
host='127.0.0.1'
#设置端口
port=12345
#绑定端口
s.bind((host, port))
#等待客户端连接
s.listen(5)
while True:
    c, addr=s.accept()    #建立客户端连接
    print '连接地址', addr
    c.send('my name is tianjingang')
    c.close()            #关闭连接
