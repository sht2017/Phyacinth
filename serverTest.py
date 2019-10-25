import socket

def main():
    s = socket.socket()
    host = '127.0.0.1'
    port = 35306
    s.bind((host, port))

    s.listen(5)
    while True:
        c,addr = s.accept()
        c.send('success'.encode('utf-8'))
        c.close()
        break

if __name__ == "__main__":
    main()