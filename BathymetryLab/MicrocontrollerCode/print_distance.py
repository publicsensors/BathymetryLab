'''
Run and print readout from an HCSR04 sensor using an ESP8266 (micropython controller)
in millimeters.  The sensor will print and read values at a given interval until
broken by the user (ctrl+c)
'''

from machine import Pin
import utime
from hcsr04 import HCSR04

sound_speed = 343
trigger_pin_num=12
echo_pin = 14
sleep_time  = 1

def print_distance(trigger_pin = trigger_pin_num, echo_pin = echo_pin_num, c=sound_speed, interval=sleep_time):
    sensor = HCSR04(trigger_pin, echo_pin, c)
    led = Pin(2, Pin.OUT)
    led.value(0)
    while True:
        led.value(1)
        print(sensor.distance())
        utime.sleep(interval)
