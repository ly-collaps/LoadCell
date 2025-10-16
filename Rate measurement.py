import time
import sys
from hx711 import HX711  # tatobari / bogde library

# Replace with your GPIO pins
DOUT = 5
SCK = 6

def cleanAndExit():
    print("Cleaning up...")
    hx.cleanAndExit()
    sys.exit()

# Initialize HX711
hx = HX711(DOUT, SCK)
hx.set_gain(128)  # Set your desired gain (128, 64, 32)

print("Measuring HX711 sampling rate... Press Ctrl+C to exit")

try:
    count = 0
    start_time = time.time()

    while True:
        if hx.is_ready():
            hx.read()  # Read one sample
            count += 1

        # Every second, print the measured SPS
        current_time = time.time()
        if current_time - start_time >= 1.0:
            print("Measured SPS: {}".format(count))
            count = 0
            start_time = current_time

        time.sleep(0.001)  # small delay to avoid 100% CPU

except (KeyboardInterrupt, SystemExit):
    cleanAndExit()
