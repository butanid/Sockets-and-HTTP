# Name: Deep Butani
# OSU Email: butanid@oregonstate.edu
# Course: CS372 - Intro to Computer Networks
# Assignment: Project 1 - Sockets and HTTP
# Due Date: 7/14/24
# Description: HTTP server program to connect and receieve data through web browser
# Sources: Computer Networking - A Top Down Approach James F. Kurose & Keith Ross (Section 2.7.2)

from socket import *

def http_server():
        # Specifying server port to connect to
        serverPort = 12000

        # Create TCP server socket using IPv4
        serverSocket = socket(AF_INET, SOCK_STREAM)
        # Bind the port number to the server socket
        serverSocket.bind(("127.0.0.1", serverPort))
        # Wait and listen for client
        serverSocket.listen(1)

        print("\nThe server is listening and ready to receive!\n")

        # Loop to receive and process packets from client
        while True:
                # Creating new socket in server dedicated to particular client
                connectionSocket, addr = serverSocket.accept()
                print(f"connectionSocket accepted connection from {addr}\n")

                # Obtain and read socket request from client
                socketRequest = connectionSocket.recv(1024).decode()
                print(f"Received request details:\n\n{socketRequest}")

                # Initialize data used for responding to client
                data =  (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=UTF-8\r\n\r\n"
                        "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
                )

                # Send resulting packet into server socket and deliver to client address
                connectionSocket.send(data.encode())
                print(data)
                # Close connectionSocket
                connectionSocket.close()

if __name__ == "__main__":
        http_server()
