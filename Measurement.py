#!/usr/bin/env python3
import time
from hx711 import HX711

DT_PIN = 5
SCK_PIN = 6
CALIBRATION_RATIO = 220.5   # replace this with your value
LEVER_ARM_LENGTH = 0.08    # meters (distance from pivot to load cell)
GRAVITY = 9.80665  # m/s^2

hx = HX711(DT_PIN, SCK_PIN)
hx.set_scale_ratio(CALIBRATION_RATIO)
hx.tare()

print("Scale ready... measuring weight, force, and torque\n")

#The main loop that runs continuously until you stop it.
try:
    while True:
        # Get average of 10 readings
        weight_g = hx.get_weight_mean(10)
        weight_kg = weight_g / 1000.0  # convert grams to kilograms

        # Calculate force in Newtons
        force_N = weight_kg * GRAVITY

        # Calculate torque (if lever arm used)
        torque_Nm = force_N * LEVER_ARM_LENGTH

        # Display results
        print(f"Mass: {weight_kg:.3f} kg | Force: {force_N:.3f} N | Torque: {torque_Nm:.3f} N·m")

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    hx.power_down()
