# TeachingMaterials

This repository serves as a central location for microcontroller projects used for both outreach and undergraduate teaching modules.  Projects are organized by either topic or sensor.

## HCSR04
The basic library and projects using the HCSR04 dual-transducer acoustic sensor controlled via micropython on an ESP8266mod microcontroller.

###  - hcsr04.py
The driver for measuring distance using the HCSR04 sensor.  Required parameters are GPIO `trigger_pin` and `echo_pin`, with optional arguments for sound speed, `c`, and timeout. Private functions to intialize the sensor parameters and send signal.  `distance` function returns distance in millimeters.

###  - HCSR04_Timer.py
Runs HCSR04 to collect distance measurements at a fixed time interval using a periodic timer, with option to write to file.

###  - HCSR04_SampleCt.py
Runs HCSR04 to collect distance measurements at a fixed time interval using user defined interval and runtime, with option to write to file.

###  - HCSR04TimeSeriesPlot.py
Reads .txt files produced by HCSR04_Timer.py or HCSR04_SampleCt.py to create time series scatter plots of distance measurements.  User must define directory of file locations.

###  - SpeedOfSoundLab.ipynb
IPython notebook containing instructions for lab activity to approximate the speed of sound in air using measurements collected at a fixed distance over variable values of `c`, sound speed.  Requires micropython firmware on ESP8266 or PyBoard microcontrollers and HC-SR04 sensor.
