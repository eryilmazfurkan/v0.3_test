import smbus2 as smbus
import time

bus = smbus.SMBus(1)
dev_addr = 0x20

conf_addr = 0x03
write_addr = 0x01

output_data = 0x00

# set as output
bus.write_byte_data(dev_addr, conf_addr, output_data)

# P7 P6 P5 P4 P3 P2 P1 P0

# TURN ON USER LED CONNECTED TO P0
bus.write_byte_data(dev_addr, write_addr, 0xFE)
time.sleep(2)
bus.write_byte_data(dev_addr, write_addr, 0xFF)
time.sleep(1)
# TURN ON USER LED CONNECTED TO P1
bus.write_byte_data(dev_addr, write_addr, 0xFD)
time.sleep(2)
bus.write_byte_data(dev_addr, write_addr, 0xFF)
time.sleep(1)
# TURN ON USER LED CONNECTED TO P2
bus.write_byte_data(dev_addr, write_addr, 0xFB)
time.sleep(2)
bus.write_byte_data(dev_addr, write_addr, 0xFF)
time.sleep(1)
# TURN ON USER LED CONNECTED TO P3
bus.write_byte_data(dev_addr, write_addr, 0xF7)
time.sleep(2)
bus.write_byte_data(dev_addr, write_addr, 0xFF)
time.sleep(1)
# TURN ON USER LED CONNECTED TO P4
bus.write_byte_data(dev_addr, write_addr, 0xEF)
time.sleep(2)
bus.write_byte_data(dev_addr, write_addr, 0xFF)
time.sleep(1)
# TURN ON USER LED CONNECTED TO P5
bus.write_byte_data(dev_addr, write_addr, 0xDF)
time.sleep(2)
bus.write_byte_data(dev_addr, write_addr, 0xFF)
time.sleep(1)
# TURN ON USER LED CONNECTED TO P6
bus.write_byte_data(dev_addr, write_addr, 0xBF)
time.sleep(2)
bus.write_byte_data(dev_addr, write_addr, 0xFF)
time.sleep(1)
# TURN ON USER LED CONNECTED TO P7
bus.write_byte_data(dev_addr, write_addr, 0x7F)
time.sleep(2)
bus.write_byte_data(dev_addr, write_addr, 0xFF)


