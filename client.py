import socket
from socket import *

while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("192.168.0.111", 7019))
    s.send(input("input('>').encode()").encode())
    var = s.recv(1024)
    print (var)