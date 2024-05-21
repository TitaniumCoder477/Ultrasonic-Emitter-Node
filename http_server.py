try:
    import usocket as socket
except:
    import socket

try:
    from micropython import machine
except:
    import machine

import time

from PowerService import PowerService
from LEDService import LEDService
from ServiceStates import ServiceStates

socketInstance = socket.socket()
socketInstance.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
addressInfo = socket.getaddrinfo("0.0.0.0", 80)
socketInstance.bind(addressInfo[0][-1])
socketInstance.listen(5)
print("INFO: Bind address info:", addressInfo)
print("INFO: Listening at http://wil-emitter-node/")

#service = LEDService(ServiceStates.getOffState())
service = PowerService(ServiceStates.getOffState())

reply = b"""\
%s

%s
"""

while True:
    reboot = False
    clientConnection = socketInstance.accept()
    clientSocket = clientConnection[0]
    clientAddress = clientConnection[1]    
    print("INFO: Client address:", clientAddress)
    print("INFO: Client socket:", clientSocket)

    clientRequest = clientSocket.readline()
    print("INFO: Request:", clientRequest)    
    decodedClientRequest = clientRequest.decode('ASCII')
    if decodedClientRequest.find("POST /on") > -1:
        print("INFO: Received an on request...")
        service.on()
        print("INFO: Here is the rest of the http request:")
        while True:
            h = clientSocket.readline()            
            if h == b"" or h == b"\r\n":
                break
            print("INFO: %s" % h)
        clientSocket.write(reply % (b"""HTTP/1.0 200 OK""", b"""Emitter is On."""))
    elif decodedClientRequest.find("POST /off") > -1:
        print("INFO: Received an off request...")
        service.off()
        print("INFO: Here is the rest of the http request:")
        while True:
            h = clientSocket.readline()            
            if h == b"" or h == b"\r\n":
                break
            print("INFO: %s" % h)
        clientSocket.write(reply % (b"""HTTP/1.0 200 OK""", b"""Emitter is Off."""))
    elif decodedClientRequest.find("GET /state") > -1:
        print("INFO: Received a state request...")
        print("INFO: Here is the rest of the http request:")
        while True:
            h = clientSocket.readline()            
            if h == b"" or h == b"\r\n":
                break
            print("INFO: %s" % h)
        clientSocket.write(reply % (b"""HTTP/1.0 200 OK""", b"""Emitter is %s""" % service.getState()))
    elif decodedClientRequest.find("POST /reboot") > -1:
        print("INFO: Received a reboot request; will handle it after closing socket...")
        reboot = True
        print("INFO: Here is the rest of the http request:")
        while True:
            h = clientSocket.readline()            
            if h == b"" or h == b"\r\n":
                break
            print("INFO: %s" % h)
        clientSocket.write(reply % (b"""HTTP/1.0 200 OK""", b"""Node will be rebooted in 5 seconds."""))
    else:
        while True:
            h = clientSocket.readline()            
            if h == b"" or h == b"\r\n":
                break
            print("INFO: %s" % h)
        clientSocket.write(reply % (b"""HTTP/1.0 400 Bad Request""", b"""Request not found."""))
    
    print("INFO: Closing socket...")
    clientSocket.close()
    print()

    if reboot == True:
        time.sleep(5)
        machine.reset()