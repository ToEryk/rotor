import socket
s = socket.socket()
port = 2222
s.bind(('', port))
s.listen(5)
while True:
    c, addr = s.accept()
    dataFromClient = c.recv(1024).decode()
    if(dataFromClient == "prawo"):
        print (dataFromClient)
        c.send("Komenda w prawo".encode())
    elif(dataFromClient == "lewo"):
        print (dataFromClient)
        c.send("Komenda w lewo".encode())
c.close()
        

    
    

    

