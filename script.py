import json
import random
import time
import socket

# Constants for pedestrian
CROSS_WIDTH = 12
CROSS_LENGTH = 6
MAX_INT = 7

# Calculate the coordinates for the top-left corner of the crosswalk
crosswalk_x = CROSS_WIDTH / 2
crosswalk_y = CROSS_LENGTH

# Set the fixed x-coordinate of the pedestrian within the crosswalk
pedestrian_x = crosswalk_x + (CROSS_WIDTH / 2)

try:
    while True:
        pedestrian_y = 0

        for i in range(MAX_INT + 1):
            # Dictionary to represent pedestrian's position
            pedestrian_position = {
                "pedestrianX": int(pedestrian_x),
                "pedestrianY": pedestrian_y,
            }

            # Creating a JSON file with pedestrian's position
            json_filename = "pedestrian_position.json"
            data = json.dumps(pedestrian_position)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            HOST, PORT = '192.168.0.2', 21
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data,encoding="utf-8"))
            sock.close()



            # Generate a random interval between iterations
            interval = random.uniform(0.5, 2.5)
            time.sleep(interval)
            print(pedestrian_y)
            pedestrian_y += 1

            if pedestrian_y > MAX_INT:
                pedestrian_y = 0  # Reset pedestrian when they reach the maximum value

except KeyboardInterrupt:
    print("User interrupted the loop.")