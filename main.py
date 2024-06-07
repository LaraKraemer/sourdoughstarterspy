# This file is executed on every boot (including wake-boot from deepsleep)
from machine import Pin
from src.hcsr04 import HCSR04
import time
import dht


# create an output pin on pin #0
led = Pin(13, Pin.OUT)
dht_sensor = dht.DHT22(Pin(14))
ultrasonic_sensor = HCSR04(trigger_pin=27, echo_pin=32)


while True:
    try:
        # Toggle LED every second
        time.sleep(1)
        led.value(1)
        time.sleep(1)
        led.value(0)
        dht_sensor.measure()


        # Read temperature and humidity
        print('Es ist %d°C bei %d%% Luftfeuchtigkeit' % (dht_sensor.temperature(), dht_sensor.humidity()))



        distance = ultrasonic_sensor.distance_cm()
        print('Distance:', distance, 'cm')


    except Exception as e:
        print("Error occurred:", e)

    finally:
        # Wait before taking the next reading
        time.sleep(10)  # Adjust delay as needed


