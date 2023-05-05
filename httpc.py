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
server_address = ('data.pr4e.org', 80)
sock.connect(server_address)

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(cmd)

"""
The script then enters a loop where it receives data from the socket using the recv() method
and prints it to the console. The recv() method blocks until data is available, or the remote end 
has closed the connection.
The loop continues until it receives data with a length greater than one (indicating that 
there is more data to receive), and then the socket is closed using the close() method.

"""

while True:
    data = sock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

sock.close()