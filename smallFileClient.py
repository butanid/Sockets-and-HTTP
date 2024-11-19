# Name: Deep Butani
# OSU Email: butanid@oregonstate.edu
# Course: CS372 - Intro to Computer Networks
# Assignment: Project 1 - Sockets and HTTP
# Due Date: 7/14/24
# Description: Simple python program that uses a socket to interact with a server
# Sources: Computer Networking - A Top Down Approach James F. Kurose & Keith Ross (Section 2.7.2)

from socket import *

# Setting up server host and port to connect to
serverName = "gaia.cs.umass.edu"
serverPort = 80

# Create TCP client socket using IPv4
clientSocket = socket(AF_INET, SOCK_STREAM)
# Initiate TCP connection between client and server
clientSocket.connect((serverName, serverPort))

# Initializing URI to make GET request to
URI = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
# Send GET request through client socket and into TCP connection
clientSocket.send(URI.encode())

# Storing response received from server
modifiedURI = clientSocket.recv(1024)

# Printing response and closing socket
print(modifiedURI.decode())
clientSocket.close()
