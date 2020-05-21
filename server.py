#!/usr/bin/python3

import socket
#Creating the socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.1.203'
host = socket.gethostname()

port = 444
#Binding the socket
serversocket.bind((host ,port))
#NO of listener or TCP Listener
serversocket.listen(3)
while True: 
    #while loop starting the connection
    clientsocket, address = serversocket.accept()

    print("recive connection from "% str(address))

    message = 'thank you for connecting the server ' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()