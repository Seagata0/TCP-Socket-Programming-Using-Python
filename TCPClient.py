from socket import * #import * dari library socket
import sys #import library sys

serverhost = 'localhost' #inisialiasi serverhost
serverport = 16265 #inisialisasi serverport

clientSocket = socket(AF_INET, SOCK_STREAM) #inisialisasi client socket memakai IPv4 & TCP
clientSocket.connect((serverhost, serverport)) #meng-establish koneksi ke server memakai serverhost & port

response = '' #inisialisasi string response
sentence = sys.argv[1] + ' ' + sys.argv[2] #membuat argument method dan filename menjadi sebuah string
clientSocket.send(sentence.encode('utf-8')) # mengirimkan sentence memakai encode utf-8 melalui clientsocket

while True: #melakukan perulangan selama true
    response += clientSocket.recv(1024).decode() #menerima response dari server dan melakukan decode lalu disimpan pada variabel response
    print(response) #melakukan print string response 
    break #stop

clientSocket.close() #menutup koneksi ke server