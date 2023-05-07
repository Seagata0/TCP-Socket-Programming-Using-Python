from socket import *
import sys

serverhost = 'localhost'
serverport = 16265

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverhost, serverport))

sentence = sys.argv[1] + ' ' + sys.argv[2]
clientSocket.send(sentence.encode('utf-8'))
response = ''

while True:
    response += clientSocket.recv(1024).decode()
    print(response)
    break

clientSocket.close()