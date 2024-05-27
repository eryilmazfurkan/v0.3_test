import board
import busio
from adafruit_tla202x import TLA2024
import time

i2c = busio.I2C(board.SCL, board.SDA)
tla = TLA2024(i2c)

while True:
    voltages = []
    for channel in range(4):
        tla.input_channel = channel
        voltages.append(tla.voltage)
    
    print("Channel 0: {:.3f} V    Channel 1: {:.3f} V    Channel 2: {:.3f} V    Channel 3: {:.3f} V".format(
          voltages[0], voltages[1], voltages[2], voltages[3]))
    
    time.sleep(1)