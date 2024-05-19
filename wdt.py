import RPi.GPIO as GPIO
import time
import subprocess
import threading
from queue import Queue


GPIO_PIN = 16
I2C_BUS = 1
DEVICE_ADDRESS = "48"
duration = 900
device_found_event = threading.Event()

"""
def setup_gpio_wdt(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    print("GPIO pin LOW yapılıyor.")

def check_i2c_device(address, timeout):
    start_time = time.time()
    while True:
        current_time = time.time()
        if current_time - start_time > timeout:
            print("120 saniye geçti ve cihaz hala bulunuyor. İşlem başarısız.")
            break

        try:
            output = subprocess.check_output(["i2cdetect", "-y", str(I2C_BUS),"0x48","0x48"], universal_newlines=True)
            if address in output:
                print(f"{address} adresindeki I2C cihazı bulundu.")
            else:
                print(f"{address} adresindeki I2C cihazı kayboldu. İşlem başarılı.")
                return True
        except subprocess.CalledProcessError as e:
            print(f"i2cdetect komutu çalıştırılırken hata oluştu: {e}")
            break

        time.sleep(1) 
"""

def gpio_control(stop_event):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    i = 1
    while not stop_event.is_set():
        GPIO.output(4, GPIO.HIGH)  
        time.sleep(2)  
        GPIO.output(4, GPIO.LOW)   
        time.sleep(28)
        print(i)
        i = i + 1 

def check_i2c_device2(stop_event, result_queue):
    time.sleep(5) 
    try:
        for _ in range(duration):
            output = subprocess.check_output(["i2cdetect", "-y", str(I2C_BUS), "0x48", "0x48"], universal_newlines=True)
            if DEVICE_ADDRESS not in output:
                print("0x48 adresi bulunamadı.")
                result_queue.put(False)
                stop_event.set()
                return 
            time.sleep(1)  
    except subprocess.CalledProcessError as e:
        print(f"Komut hatası: {e}")
        result_queue.put(False)
        stop_event.set()
        return

    if not stop_event.is_set():
        print("0x48 hiç kaybolmadı.")
        result_queue.put(True)
    
    stop_event.set()

def wdt_control():
    stop_event = threading.Event()
    result_queue = Queue()
    
    gpio_thread = threading.Thread(target=gpio_control, args=(stop_event,))
    i2c_thread = threading.Thread(target=check_i2c_device2, args=(stop_event, result_queue))
    
    i2c_thread.start()
    gpio_thread.start()
    
    i2c_thread.join()
    gpio_thread.join()
        
    result = result_queue.get() if not result_queue.empty() else False
    print(f"Sonuç: {result}")

    return result
 
wdt_control()

