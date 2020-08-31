# BathymetryLab

This repository serves as a central location for the ultrasonic distance sensor Bathymetry Lab module and related activities for both outreach, K-12, and undergraduate teaching.

## **ESP8266**
The basic libraries and codes using the HC-SR04 or JSN-SR04T acoustic sensor controlled via micropython on an ESP8266 processor microcontroller such as the [HUZZAH ESP8266 Breakout](https://www.adafruit.com/product/2471).

###  hcsr04.py
The driver for measuring distance using the HCSR04 sensor.  Required parameters are GPIO `trigger_pin` and `echo_pin`, with optional arguments for sound speed, `c`, and timeout. Private functions to intialize the sensor parameters and send signal.  `distance` function returns distance in millimeters.

### firmware-combined.bin
Micropython firmware for ESP8266 boards. See [Getting started with MicroPython on the ESP8266](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html) for details on deploying the firmware.

### boot.py
Basic boot initialization file example.

### print_distance.py
Using the hcsr04 driver to continuously measure and print distance at set interval.

### record_distance.py
Using the hcsr04 driver to continuously measure distance at set interval and record to a text file. The output file can be read by the `plot_recorded_distance.py` script. Calling, as commented in the file, is completed as:
```Python
import record_distance
prefix = 'NAME'
interval_ms = 1 # sampling interval in milliseconds, 100 is 10Hz
record_time = 10 # time to record in seconds
trigger_pin_num = 12 # trigger pin connection to HCSR04 sensor
echo_pin_num = 14 # echo pin connection to HCSR04 sensor
sound_speed = 343 # Sound speed in m/s
write_file = 1

record_distance.record_dist(prefix,interval_ms,record_time, trigger_pin_num, echo_pin_num, sound_speed, write_file)
```

## **ActivityNotebooks**
### AcousticSensorLab.ipynb
IPython notebook containing instructions for two lab activities:
1.  Approximate the speed of sound in air using measurements collected at a fixed distance over variable values of `c`, sound speed.  Requires micropython firmware on ESP8266 or PyBoard microcontrollers and HC-SR04 sensor.
2.  Measure and map the change in seafloor using a JSN-SR04T waterproof transducer.  Students collect data at fixed intervals along a dock or pier and then create a plot of the bathymetry using python on their own computers.

### AcousticSensorLabHandout.ipynb
Contains all of the instructions for students to complete the assignment, but leaves out example executable code and data for figures.

### AcousticSensorLabPyserial.ipynb
Identical lab activity to `AcousticSensorLab.ipynb` however the notebook utilizes `pyserial` to record measurements directly from a USB-connected ESP8266 rather than requiring students to input readings by hand.

## **WaveTankLab**
Code for conducting an extension activity using multiple distance sensors to measure wave height at different positions in a wave tank. Students explore signal processing and implications of variable sampling frequencies.

### HCSR04_Timer.py
Runs HCSR04 to collect distance measurements at a fixed time interval using a periodic timer, with option to write to file.

###  HCSR04_TrigRx.py
Runs HCSR04 to collect distance measurements at a fixed time interval using a periodic timer, with option to write to file.  The timer is initiated from an external interrupt.

###  xcorrTimeSeries.py
Reads .txt files produced by HCSR04_Timer.py or HCSR04_SampleCt.py to create time series scatter plots of distance measurements.  User must define directory of file locations.
