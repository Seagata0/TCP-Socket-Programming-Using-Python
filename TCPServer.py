from socket import * #import * dari library socket

serverhost = 'localhost' #inisialiasi serverhost
serverport = 16265 #inisialisasi serverport

serverSocket = socket(AF_INET, SOCK_STREAM) #inisialisasi server socket memakai IPv4 & TCP
serverSocket.bind((serverhost, serverport)) #melakukan bind serverhost dan serverport ke serversocket
serverSocket.listen() #serversocket melakukan listen untuk menunggu request koneksi dari client

def sendtoclient(connectionSocket, status_code, status_text, file_content): #function untuk mengirimkan data beserta header ke client
    response = "HTTP/1.1 {} {}\r\n\r\n{}".format(status_code, status_text, file_content) #membuat response header dan file
    connectionSocket.send(response.encode('utf-8')) #mengirimkan response ke client

while True: #melakukan perulangan selama true
    print("Hello!") 
    print("The server is ready to serve you") #print untuk menandakan bahwa server siap melayani client

    connectionSocket, addr = serverSocket.accept() #menerima koneksi dan memasukkan data socket client ke variabel connectionSocket dan address client ke variabel addr
    msg = connectionSocket.recv(1024).decode() #menerima pesan dari client dan melakukan decode
    print('============================================================') 
    print('There is an incoming Message!') 
    print('=============================')
    print('Message : ', msg) #melakukan print isi pesan
    print('Type of connectionSocket : ', type(connectionSocket)) #melakukan print tipe koneksi
    print('Socket type : ', connectionSocket.type) #melakukan print tipe socket
    print('Socket name : ', connectionSocket.getsockname()) #melakukan print nama socket
    print('Address : ', addr) #melakukan print address client

    lst = msg.split(' ') #melakukan split isi pesan dan menyimpannya pada list lst
    method = lst[0] #mengambil method dari index 0
    filename = lst[1] #mengambil filename dari index 1
    print('Method : ', method) #melakukan print metode yang diminta oleh client
    print('Filename : ', filename) #melakukan print filename yang di request

    try: #akan mencoba code dibawah
        if (filename[0] == '/' and len(filename)==1): # jika filename index 0-nya adalah / dan lenght nya = 1 maka open index.html karena client melakukan request dari browser tanpa memasukan nama file yang ingin di akses
            f = open('index.html') #open file index.html
        elif (filename[0] == '/'): #jika filename filename index 0-nya adalah / 
            filename = filename[1:] #filenamennya dimulai dari index 1 bukan dari 0
            f = open(filename) #open filename yang di request
        else : #jika bukan keduanya
            f = open(filename) #open filename yang di request
        
        file_content = f.read() #inisialisasi file_content yang berisi data dari f yang telah di read
        outputdata = f #inisialisasi outputdata yang berisikan isi dari variabel f
        print('\nopen() output : ', outputdata) #melakuak print outputdata
        sendtoclient(connectionSocket, 200, 'OK', file_content) #memanggil function sendtoclient untuk mengirim file content
        print('successfully sent ',filename,' to the client\n') #pemberitahuan jika file content berhasil dikirim
        print('============================================================\n\n')
    
    except IOError:
        print('\ncouldnt open the file or couldnt found the file \n sending error message to the client') #print pesan error
        if (len(lst)==2): #jika lenght dari list = 2 menandakan request berasal dari TCPClient.py
            error_content = '\nSo Stupid, you type wrong file Failure!\n' #inisialisasi error_content
            sendtoclient(connectionSocket, 404, 'Not Found', error_content) #mengirimkan error_content menuju ke client
        else:
            error_file = open("404.html") #open 404.html lalu simpan ke variabel error_file
            error_content = error_file.read() #membaca isi error_file untuk dijadikan error content
            sendtoclient(connectionSocket, 404, 'Not Found', error_content) #mengirimkan error_content menuju ke client
        print('============================================================\n\n')
        
    connectionSocket.close() #menutup koneksi socket antara server dan client
