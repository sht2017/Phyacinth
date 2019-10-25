import getIP,clientTest,serverTest,multiprocessing
def main():
    #ip=getIP.main()
    ip='127.0.0.1'
    print('ip='+ip)
    #print(clientTest.main('',ip))
    serverTestProcess=multiprocessing.Process(target=serverTest.main,args=())
    print('#1')
    clientTestProcess=multiprocessing.Process(target=clientTest.main,args=(multiprocessing.Queue(),ip))
    serverTestProcess.start()
    print('#2')
    clientTestProcess.start()
    while clientTestProcess.is_alive():
        print(multiprocessing.Queue().get(True))
        serverTestProcess.terminate()
    print('#3')

if __name__ == "__main__":
    main()