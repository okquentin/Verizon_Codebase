import time

# Define the maximum integer and the interval
MAX_INT = 6
INTERVAL = 1  # in seconds
while True:
# Initialize a counter
    counter = 0
    # Use a for loop with range() to increment the counter
    for i in range(0, MAX_INT, INTERVAL):
        time.sleep(INTERVAL)
        counter += 1
        print(counter)
