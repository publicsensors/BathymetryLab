# BathymetryLab
## **MaterialsForInstructors**
### BathymetryLab_Instructor.ipynb
IPython notebook containing instructions and example figures for the bathymetry lab activity.
___
## **Handouts**
### BathymetryLab.ipynb
IPython notebooks for use to measure and map the change in seafloor using a JSN-SR04T waterproof transducer.  Students collect data at fixed intervals along a dock or pier and then create a plot of the bathymetry using python on their own computers. `BathymetryLab.ipynb` is the empty activity notebook.

### BathymetryLab_Pyserial.ipynb
Identical lab activity to `BathymetryLab.ipynb` however the notebook utilizes `pyserial` to record measurements directly from a USB-connected ESP8266 rather than requiring students to input readings by hand.
___
## **Microcontroller**
This folder contains the basic libraries and codes for using the HC-SR04 or JSN-SR04T acoustic sensor via MicroPython, though alternative microcontroller systems can be used to conduct the activity. Examples and code in this repository are for use with an ESP8266 processor microcontroller such as the [Feather HUZZAH with ESP8266](https://www.adafruit.com/product/2821).

Another example of sensor assembly using a [Feather STM32F405 Express](https://www.adafruit.com/product/4382) and [PyBoard](https://store.micropython.org/) microcontrollers can be found in the [Microcontroller Kits repository](https://github.com/publicsensors/MicrocontrollerKits/tree/master/Sensors/Acoustic) within the PublicSensors organization.

####  hcsr04.py
The driver for measuring distance using the HCSR04 sensor.  Required parameters are GPIO `trigger_pin` and `echo_pin`, with optional arguments for sound speed, `c`, and timeout. Private functions to intialize the sensor parameters and send signal.  `distance` function returns distance in millimeters.
```python
import hcsr04
sensor = hcsr04.HCSR04(trigger_pin=12, echo_pin=14, c=343) # define pins and speed of sound
sensor.distance() # returns distance in mm
```

#### firmware-combined.bin
Micropython firmware for ESP8266 boards. See [Getting started with MicroPython on the ESP8266](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html) for details on deploying the firmware.

#### boot.py
Basic boot initialization file example.

#### print_distance.py
Using the `hcsr04.py` driver to continuously measure and print distance at set interval.
```python
import print_distance
print_distance.print_distance(trigger_pin = 12, echo_pin = 14, c=343, interval=1) #interval is time in seconds
```
### SensorPartsList.xlsx
Excel spreadsheet with details and approximate pricing for sensor components needed to conduct the activity. Additional recommendations and instructions on assembly specific to this activity are found in the **MaterialsForInstructors** folder.
