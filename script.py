import json
import random
import time
import socket

XCOORD = 225
yCoord = 0

while True:
    while yCoord < 126:
        pedestrian = { 
            "carX": yCoord,
            "carY": XCOORD
         }
        pCoords = json.dumps(pedestrian)
        HOST = '192.168.0.2'
        PORT = 21
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.connect((HOST, PORT))
        # sock.sendall(bytes(pCoords, 'utf-8'))
        # sock.close()
        print(yCoord)
        yCoord += 1
        time.sleep(.75)
    yCoord = 0
    waitTime = random.randint(0,7)
    time.sleep(waitTime)