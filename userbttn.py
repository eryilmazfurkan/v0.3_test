import RPi.GPIO as GPIO
import time

button_pin = 5

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        button_state = GPIO.input(button_pin)
        
        if button_state == GPIO.LOW:
            print("Buton basıldı!")
            break
        else:
            print("Buton basılı değil.")
        
        
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
