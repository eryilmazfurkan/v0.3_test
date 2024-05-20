import serial
import time

ser = serial.Serial('/dev/ttyUSB2', baudrate=115200, timeout=1)

ser.write(b'AT+QGPS=1\r')
time.sleep(2)

ser.write(b'AT+QGPSLOC=0\r')
time.sleep(10)

response = ser.read(100)
print(response.decode('utf-8'))

ser.write(b'AT+QGPSEND\r')

ser.close()

