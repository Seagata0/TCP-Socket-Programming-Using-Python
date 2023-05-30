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
    print("Hello, how are yu")
    print("I am under the water")
    print("Please help me")
    print("There is too much rain whoooo")
    print("\nThe server is ready to serve you")

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
        if (filename[0] == '/' and len(filename)==1):
            f = open('index.html')
        elif (filename[0] == '/'):
            f = open(filename[1:])
            filename = filename[1:]
        else :
            f = open(filename)
        
        file_content = f.read()
        outputdata = f
        print('\nopen() output : ', outputdata)
        sendtoclient(connectionSocket, 200, 'OK', file_content)
        print('\n\tsuccessfully sent %s to the client\n' % (filename))
    
    except IOError:
        print('\n\tcould not open the file...\n\n\t...error message to the requester\n\n')
        if (len(lst)==2):
            error_content = '\nSo Stupid, you type wrong file Failure!\n'
            sendtoclient(connectionSocket, 404, 'Not Found', error_content)
        else:
            error_file = open("404.html")
            error_content = error_file.read()
            sendtoclient(connectionSocket, 404, 'Not Found', error_content)
        
    connectionSocket.close()
