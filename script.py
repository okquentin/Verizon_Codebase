import json
import socket
import random
import time

YCOORD = 3
xCoord = 0
speed = 30

while True:
    while xCoord < 11:
        car = { 
            "carX": xCoord,
            "carY": YCOORD
         }
        cCoords = json.dumps(car)
        HOST = '192.168.0.2'
        PORT = 21
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.sendall(bytes(cCoords, 'utf-8'))
        sock.close()
        print(xCoord)
        xCoord += 1
        time.sleep(1)
    xCoord = 0
    waitTime = random.randint(0,7)
    time.sleep(waitTime)