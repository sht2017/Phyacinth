from multiprocessing import Process, Queue
import getIP,clientTest,serverTest,options

def main():
    if options.debugMode:
        ip='127.0.0.1'
    else:
        ip=getIP.main()
    
    print('ip='+ip)
    serverTestProcess=Process(target=serverTest.main,args=())
    returnData=Queue()
    clientTestProcess=Process(target=clientTest.main,args=(returnData,ip))
    serverTestProcess.start()
    clientTestProcess.start()
    returnData = returnData.get()
    clientTestProcess.join()
    serverTestProcess.terminate()
    if returnData == 0:
        exit()


if __name__ == "__main__":
    main()