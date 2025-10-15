# ------------ Calibration------------------------
# Calibration determines the scale factor (how many raw units = 1 gram)

#!/usr/bin/env python3
import time
import sys
from hx711 import HX711

# Set your GPIO pins here
DT_PIN = 5   # DOUT
SCK_PIN = 6  # SCK

# Create an HX711 object to handle communication with your sensor
hx = HX711(DT_PIN, SCK_PIN)

# Safe shutdown function: called when the script ends normally or is interrupted
def cleanAndExit():
    print("Cleaning up...")
    hx.power_down()
    hx.power_up()
    sys.exit()

try:
    print("Initializing... remove all weight from the load cell.")
    time.sleep(2)
    hx.reset()
    hx.tare()
    print("Tare done. Place a known weight on the scale.")

    known_weight = float(input("Enter the known weight in grams (e.g. 500): "))

    print("Reading values...")
    time.sleep(2)
    reading = hx.get_data_mean(10)  #takes 10 samples from the HX711 and averages them.

    if reading:
        print(f"Raw average reading: {reading}")
        ratio = reading / known_weight
        print(f"Calculated calibration ratio (scale): {ratio}")
        print("Use this ratio in your measurement code as set_scale_ratio().")
    else:
        print("No valid reading received.")
    cleanAndExit()

except (KeyboardInterrupt, SystemExit):
    cleanAndExit()
