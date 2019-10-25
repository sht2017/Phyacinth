def textProcess(text):
    return '\033[1;37;41m'+"%03d"%text+'\033[0m'
    pass

def main(error):
    error=int(error)
    if error==0:
        print('Get public ip address successfully')
        return 1
    elif error==1:
        print('ERROR_CODE:'+textProcess(error))
        print('Your computer have no public ip address')
        return 0
    elif error==2:
        print('ERROR_CODE:'+textProcess(error))
        print('Time out')
        return 0
    elif error==3:
        print('ERROR_CODE:'+textProcess(error))
        print('Unable to process this type of data')
        return 0
    else:
        print('ERROR_CODE '+textProcess(error)+' is not defined')
        
if __name__ == "__main__":
    import sys
    main(sys.argv[1])