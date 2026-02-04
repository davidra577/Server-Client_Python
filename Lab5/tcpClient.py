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
    s.connect((host, port))

    message = input("->")
    byte = message.encode()
    while message != 'q':
        s.send(byte)
        data = s.recv(1024)
        print('Received from server: ' + str(data.decode('utf-8')))
        message = input("->")
        byte = message.encode()
    s.close()

if __name__ == '__main__':
    Main()
