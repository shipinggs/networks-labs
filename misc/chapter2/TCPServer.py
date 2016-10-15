from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print "The server is ready to receive"

while 1:
    connectionSocket, clientAddr = serverSocket.accept()
    while 1:
        message = connectionSocket.recv(2048)
        returnMessage = message.upper()
        connectionSocket.send(returnMessage)
