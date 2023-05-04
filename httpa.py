# sockets in python
"""
The socket module provides low-level networking interfaces that allow you to create and 
interact with network sockets. Sockets are a fundamental concept in network programming 
and are used to establish connections between processes running on different machines 
or on the same machine.

To create a socket, you need to call the socket() function and specify the address family 
and socket type. The address family can be either AF_INET for IPv4 or AF_INET6 for IPv6, 
while the socket type can be SOCK_STREAM for TCP or SOCK_DGRAM for UDP. 

"""
import socket

# create a TCP/IP socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

"""
Once you have a socket object, you can use it to send and receive data over the network. 
For example, to connect to a server and send a message over TCP:

"""

# connect the socket to a remote server 
server_address = ('localhost', 8888)
sock.connect(server_address)

# send a message
message = b'Hello, server!'
sock.sendall(message)

# receive a response
data = sock.recv(1024)
print(data.decode('utf-8'))

# close the socket
sock.close()

"""
Note that in this example, we're using the b prefix to indicate that the message is a bytes object, 
since sockets operate on bytes rather than strings. We also need to specify the encoding when 
decoding the received data using the decode() method.

"""

