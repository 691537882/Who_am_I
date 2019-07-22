#此示例为服务器
import socket
address = ('0.0.0.0',9999)

#创建socket
server = socket.socket()

#绑定地址：bind()函数
server.bind(address)

#监听 listen(),10表示：如果服务器没有能力去接收的话，后面可以有多少个队列在此等候
server.listen(10)
print('服务器已启动',address)

#接收请求：accept()函数，接收服务器的请求，这个时候在这儿会形成阻塞，也叫阻塞函数。如果没有客户端连接，它会
#在这一直等，等到有客户端连接时，这个时候才会有返回值，
#sockfd是返回的新的套接字，刚刚我们创建的套接字叫server，它是用来监听的，而返回的这个则是用来进行数据传输的
#addr就是客户端返回的地址
sockfd,addr = server.accept()

#接收完之后，可以打印一下
print('收到客户端连接请求：',addr)

#数据的收发，recv（）,1024表示最大接收的1024个字节
data =sockfd.recv(1024)
#网络上的数据是经过编码或是格式转化的，decode是要将它格式转回来
print(data.decode())
#关闭连接
sockfd.close()
server.close()

















