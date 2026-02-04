import socket
# name:David Ra
# student id= 101977205
# email dra@myseneca.ca
# DCF255NDD
# youtube source used : https://www.youtube.com/watch?v=XiVVYfgDolU&feature=youtu.be
# written in python 3.8 (latest)
def Main():
    host = '127.0.0.1'
    port = 55955

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("from connected user: " + str(data.decode('utf-8')))
        data = str(data.decode('utf-8')).upper()
        print("sending: " + str(data))
        byte = data.encode()
        c.send(byte)
    c.close()

if __name__ == '__main__':
    Main()
    
