#
#  Collect data from an HCSR04 ultrasonic sensor by setting a timer to sample at
# a fixed interval for a given length of recording
#
from machine import RTC, Pin, Timer, unique_id
import utime
from ubinascii import hexlify
from gc import collect
from hcsr04 import HCSR04
from os import rename, listdir
collect()      # Free up heap space

"""
Before calling HCSR04_TrigRx, the rtc on the ESP8266 must be synced with NTP:
>>> import ntptimeTS3231
>>> ntptimeTS3231.settime()

#  An example of a typical execution sequence:
#---------------------------------------
# Sampling parameters
#---------------------------------------

import HCSR04_TrigRx

prefix = 'robert'
interval_ms = 100 # sampling interval in milliseconds, 100 is 10Hz
record_time = 10 # time to record in seconds
trigger_pin_num = 12 # trigger pin connection to HCSR04 sensor
echo_pin_num = 14 # echo pin connection to HCSR04 sensor
sound_speed = 343 # Sound speed in m/s
write_file = 0 # 0 to just print values, 1 to save to text file with file prefix defined above

HCSR04_TrigRx.measure_dist(prefix,interval_ms,record_time, trigger_pin_num, echo_pin_num, sound_speed, write_file)

"""
led = Pin(2,Pin.OUT)

def measure_dist(prefix='ocn351',interval_ms=100, trigger_pin_num = 12, echo_pin_num=14, sound_speed=343, write_file = 0):
	sensor = HCSR04(trigger_pin = trigger_pin_num, echo_pin = echo_pin_num, c=sound_speed) # Set up the HCSR04
        print('\nUsing sampling interval ',interval_ms,' milliseconds...')
	print('Recording data for ',record_time,' seconds...\n')
	print('\n\n****Beginning Recording ****\n\n')
	runTimer = Timer(-1) # Initiate a timer
	tmp_file='tmp.txt'  # A temporary filename; we will write partial data to this file, and rename only if sampling
	rtc = RTC() # intiate a real-time clock variable
	ID=hexlify(unique_id()).decode('utf-8') # Unique ID of the microprocessor
	timestamp=str(utime.mktime(rtc.datetime())) # Create a string time stamp from the real-time clock
	filename=prefix+'_'+ID+'_'+timestamp+'.txt' # Define a filename to be used if writing a file
	if write_file ==1: # If writing a file...
		print('\nCreating data file: ',filename,'\n\n') # Notify user
		datafile=open(tmp_file,'w')  # Create and open a temporary file for data to be logged to
	else: # if not writing a file...
		datafile='' # Create an empty variable to be passed along
		print('\nNot writing data to file\n') # Notify user
	# Run a timer that executes our record_dist function periodically, with the interval of the period defined from interval_ms
	p13 = Pin(13, Pin.IN) # define my interrupt input
	p13.irq(trigger=Pin.IRQ_FALLING, handler=init_record(sensor,write_file, tmp_file, rtc, datafile, filename)) # set the trigger
	print('\nWaiting For Trigger\n')


def init_record(sensor,write_file, tmp_file, rtc, datafile, filename):
	runTimer.init(period=interval_ms, mode=Timer.PERIODIC, callback=lambda t:record_dist(sensor,write_file, tmp_file, rtc, datafile))
	utime.sleep(record_time) # Sleep and let the timer run for the length of time defined by record_time
	runTimer.deinit() # At the end of our sleep, stop the timer
	if write_file ==1:	# If we've been writing a file...
		datafile.close() # Close the temporary file
		rename(tmp_file,filename) # Rename the temporary file with the filename constructed above


# The actual function taking a measurement and recording the time
def record_dist(sensor,write_file, rtc, datafile): # requires the sensor, real-time clock, and datafile handles, and whether we are writing a file
	led.value(0)
	t_onboard=rtc.datetime() # Get the time
	dist = sensor.distance() # take a distance measuremen
	if write_file ==1: # If saving the data...
		data_str='' # Initiate a string to add values to
		for t in [t_onboard[0],t_onboard[1],t_onboard[2],t_onboard[4],t_onboard[5],t_onboard[6],t_onboard[7], dist]: # for each value in the date string plus measurement...
			data_str+='{} '.format(t) # Combine all of the values into one line
		df=datafile.write("%s\n" % data_str) # What that line and a line-break into our file
	# Whether writing a file or not, print the time and measurement for the user to see
	print(t_onboard[0],t_onboard[1],t_onboard[2],t_onboard[4],t_onboard[5],t_onboard[6],t_onboard[7], dist)
	led.value(1)
