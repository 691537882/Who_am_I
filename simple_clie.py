#客户端

import socket
#第个参数：本机的回环地址
address = ('127.0.0.1',9999)

#创建socket
client = socket.socket()

#连接服务器  connect函数
client.connect(address)

#发送数据
msg = '这是一个测试消息'
#encode，转换成网络上传输的格式
client.send(msg.encode())
print('消息已经发送')
#关闭连接
client.close()























