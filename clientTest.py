import socket,errorCodeProcess

def main(queue,target):
    target=str(target)
    s = socket.socket()
    port = 35306
    error=0
    print('t1')
    try:
        s.connect((target, port))
        msg=s.recv(1024).decode()
        s.close()
        print('t2')
    except ConnectionRefusedError:
        error=1
    except TimeoutError:
        error=2
    else:
        if msg == 'success':
            error=0
        else:
            error=3

    if queue!='':
        print('t3')
        queue.put(error)
    
if __name__ == "__main__":
    import sys
    main(sys.argv[1])