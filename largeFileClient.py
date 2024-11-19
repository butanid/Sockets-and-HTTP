# Name: Deep Butani
# OSU Email: butanid@oregonstate.edu
# Course: CS372 - Intro to Computer Networks
# Assignment: Project 1 - Sockets and HTTP
# Due Date: 7/14/24
# Description: Socket program to receive arbitrarily large files
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
URI = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
# Send GET request through client socket and into TCP connection
clientSocket.send(URI.encode())

# Citation for the following function:
# Date Accessed: 7/12/24
# Code below is a modified version from a stack overflow example
# Source URL: https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data

# Initializing response buffer to store data
data = b""

# Loop to receieve data in chunks
while True:
    # Storing response received from server
    modifiedURI = clientSocket.recv(1024)
    # Checks if no more data left to receive and breaks loop
    if not modifiedURI:
        break
    # Appending chunk of data to response buffer
    data += modifiedURI

# Printing response and closing socket
print(data.decode())
clientSocket.close()
