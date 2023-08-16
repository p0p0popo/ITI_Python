def read(path,option):
    data=''
    
    try:
        f=open(path,'r')
    except ValueError as err:
        print(str(err))
        return 

    if f.readable():
        if(isinstance(option,int)):
            data=f.read(option)
        elif(option=='all'):
            data=f.read()
        elif(option=='line'):
            data=f.readline()
        elif(option=='lines'):
            data=f.readlines()
        else:
            data='option mistake '
    else :
        print("can't read file")
    f.close()
    return data


def write(path,content):
    f=open(path,'w')
    if f.writable:
        f.write(content)
    else:
        print("permission denied")
    f.close()


