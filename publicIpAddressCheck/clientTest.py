import socket,errorCodeProcess

def main(queue,target):
    target=str(target)
    s = socket.socket()
    port = 35306
    error=0
    try:
        s.connect((target, port))
        msg=s.recv(1024).decode()
        s.close()
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
        queue.put(errorCodeProcess.main(error))
    else:
        return errorCodeProcess.main(error)

if __name__ == "__main__":
    import sys
    if main('',sys.argv[1]) == 0:
        print('not support')
    else:
        print('support')