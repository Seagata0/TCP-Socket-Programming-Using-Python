from socket import *
serverhost = 'localhost'
serverport = 16265

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverhost, serverport))
serverSocket.listen()

def sendtoclient(connectionSocket, status_code, status_text, file_content):
    response = "HTTP/1.1 {} {}\r\n\r\n{}".format(status_code, status_text, file_content)
    connectionSocket.send(response.encode('utf-8'))

while True:
    print("ごきげんよう、ご主人様")
    print("The server is ready to serve you")

    connectionSocket, addr = serverSocket.accept()
    msg = connectionSocket.recv(1024).decode()
    print('Incoming message : ', msg)
    print('Type of connectionSocket : ', type(connectionSocket))
    print('Socket type : ', connectionSocket.type)
    print('Socket name : ', connectionSocket.getsockname())
    print('Address : ', addr, '\n\n')

    lst = msg.split(' ')
    if(lst[0]):
        method = lst[0]
    if (lst[1]):
        filename = lst[1]

    print('method : ', method)
    print('filename : ', filename)

    try:
        if (filename[0] == '/'):
            f = open(filename[1:])
            filename = filename[1:]
        else :
            f = open(filename)
        
        file_content = f.read()
        outputdata = f
        print('\nopen() output : ', outputdata)

        sendtoclient(connectionSocket, 200, 'OK', file_content)

        print('\n\tsuccessfully sent %s to the requester\n' % (filename))
    
    except IOError:
        print('\n\tcould not open the file...\n\n\t...error msg to the requester\n\n')
        if (len(lst)==2):
            error_content = '\nHTTP/1.1\n404\nSomething went wrong, only a programmer can fix it...\n'
            connectionSocket.send(error_content.encode('utf-8'))
        else:
            error_content = '<html><body><h1>404 Not Found</h1></body></html>'
            sendtoclient(connectionSocket, 404, 'Not Found', error_content)
        
    connectionSocket.close()