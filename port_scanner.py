# Will Goodrum (wcg9ev)
import socket
import datetime


def fixInputtoIP(target): # changes a domain input to an ip address if it looks like one
    for i in range(len(target)):
        if target[i].isalpha():
            i = len(target)
            target = socket.gethostbyname(target)

    return target


def getTarget(): # gets domain/ip from user input and checks if it looks like an address
    target = input("Enter target DomainName or IP >> ")
    if not ('.' in target):
        raise Exception("!!!target does not look like a domain/ip!!!")

    return fixInputtoIP(target)


def getPortRange(): # gets upper and lower bounds on port scan, ensures bounds are valid
    lowerPort = int(input("Enter lowerBound for portScan >> "))
    upperPort = int(input("Enter upperBound for portScan >> "))
    if not (lowerPort < upperPort):
        raise Exception("!!!invalid lower and upper bound!!!")

    return lowerPort, upperPort


def portScan(ip, lower, upper): # iteratively scans all ports in range given for the ip given
    for i in range(lower, upper):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1) # time out set to one second
            status = s.connect_ex((ip, i))
            if status == 0:
                print(f"Port {i}: Open")
            else:
                print(f"Port {i}: Closed")
            s.close()
        except socket.gaierror: # ends scan if ip is bad
            raise Exception("!!!hostName couldn't be resolved!!!")
        except socket.timeout: # currently doesn't work, don't know why as this is the exception name
            print(f"Port {i}: timeOut")
        except socket.error:
            print(f"Port {i}: error")


def main():
    ip = getTarget()
    ports = getPortRange()
    time = datetime.datetime.now()
    print(f"Commencing scan, current time: {time}")
    portScan(ip, ports[0], ports[1])
    time = datetime.datetime.now()
    print(f"Scan completed, current time: {time}")


main()
