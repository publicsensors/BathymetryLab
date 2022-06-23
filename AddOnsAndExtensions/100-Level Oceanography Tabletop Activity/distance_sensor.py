# Function to return distance (mm) from an HCSR-04 Utrasonic Acoustic sensor
# Written for Ocean 161, Sensing with Sound Lab
# S. Seroy, Oceanography, Univ. of Washington
# Oct 28, 2021


def read_distance(speed = 343):

    # Import modules
    import hcsr04
    from machine import Pin

    # Pin assignments
    trig = "X10"
    echo = "X9"

    # Set up the sensor
    sensor = hcsr04.HCSR04(trig, echo, speed)
    print(sensor.distance())


def read_distance_continuous(speed = 343):

    # Import modules
    import hcsr04
    import time
    from machine import Pin

    # Pin assignments
    trig = "X10"
    echo = "X9"

    # Set up the sensor
    sensor = hcsr04.HCSR04(trig, echo, speed)
        
    while True:
        print(sensor.distance())
        time.sleep(1)
