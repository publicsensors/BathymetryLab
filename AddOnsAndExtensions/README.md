# AddOnsAndExtensions

## **SpeedOfSound**
### SpeedOfSound_Instructor.ipynb
IPython notebook containing instructions and example figures for a lab activity to approximate the speed of sound in air using measurements collected at a fixed distance over variable values of `c`, sound speed.  Requires micropython firmware on ESP8266 or PyBoard microcontrollers and HC-SR04 sensor. `SpeedOfSound.ipynb` is the empty activity notebook.

### SpeedOfSound.ipynb
Contains all of the instructions for students to complete the assignment described above, but leaves out example executable code and data for figures.

### SpeedOfSound_Pyserial.ipynb
Identical lab activity to `SpeedOfSound.ipynb` however the notebook utilizes `pyserial` to record measurements directly from a USB-connected ESP8266 rather than requiring students to input readings by hand.

---

## **WaveTankLab**
Code for conducting an extension activity using multiple distance sensors to measure wave height at different positions in a wave tank. Students explore signal processing and implications of variable sampling frequencies.

### HCSR04_Timer.py
Runs HCSR04 to collect distance measurements at a fixed time interval using a periodic timer, with option to write to file.

###  HCSR04_TrigRx.py
Runs HCSR04 to collect distance measurements at a fixed time interval using a periodic timer, with option to write to file.  The timer is initiated from an external interrupt.

###  xcorrTimeSeries.py
Reads .txt files produced by HCSR04_Timer.py or HCSR04_SampleCt.py to create time series scatter plots of distance measurements.  User must define directory of file locations.

---

## **AdditionalCode**
Extra materials for reading and plotting recorded files.

### plot_recorded_distance.py
Reads and plots time series of distance data recorded in text file using `HCSR04_Timer.py` in the **WaveTankLab** or `record_distance.py`.

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
