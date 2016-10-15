from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while 1:
    message = raw_input('Please input a message: ')
    clientSocket.send(message)
    serverMessage  = clientSocket.recv(2048)
    print 'Modified message: ' + serverMessage
