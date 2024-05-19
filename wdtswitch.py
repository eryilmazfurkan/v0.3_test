import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  

try:
    while True:
        switch_state = GPIO.input(8)  
        if switch_state == GPIO.HIGH:
            print("Switch ON")
        else:
            print("Switch OFF")
        time.sleep(0.1)  

except KeyboardInterrupt:
    print("Program sonlandırıldı")

finally:
    GPIO.cleanup() 
