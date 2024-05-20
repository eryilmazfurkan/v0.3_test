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

bus.write_byte_data(dev_addr, write_addr, 0x02)
time.sleep(5)
bus.write_byte_data(dev_addr, write_addr, 0xFD)

time.sleep(2)

bus.write_byte_data(dev_addr, write_addr, 0x01)
time.sleep(5)
bus.write_byte_data(dev_addr, write_addr, 0xFD)

time.sleep(2)

bus.write_byte_data(dev_addr, write_addr, 0xDB)
time.sleep(5)
bus.write_byte_data(dev_addr, write_addr, 0xFD)

time.sleep(2)

bus.write_byte_data(dev_addr, write_addr, 0xB4)
time.sleep(5)
bus.write_byte_data(dev_addr, write_addr, 0xFD)

time.sleep(2)

bus.write_byte_data(dev_addr, write_addr, 0x6D)
time.sleep(5)
bus.write_byte_data(dev_addr, write_addr, 0xFD)

