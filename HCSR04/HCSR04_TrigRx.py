#
#  Collect data from an HCSR04 ultrasonic sensor by setting a timer to sample at
# a fixed interval for a given length of recording
   # Free up heap space

"""
# Before calling HCSR04_TrigRx, the rtc on the ESP8266 must be synced with NTP:

from network import WLAN, STA_IF
wlan = WLAN(STA_IF)
wlan.active(True)
wlan.connect('OTCnet','ocN3five1_OTc')
import ntptimeTS3231
ntptimeTS3231.settime()

# Once the onboard clock is set, we have to define all of the parameters for running
#  An example of a typical execution sequence:
#---------------------------------------
# Sampling parameters - must be defined
#---------------------------------------
 	
import HCSR04_TrigRx

prefix = 'Position2_SlowWave'
interval_ms = 100 # sampling interval in milliseconds, 100 is 10Hz
record_time = 60 # time to record in seconds
trigger_pin_num = 12 # trigger pin connection to HCSR04 sensor
echo_pin_num = 13 # echo pin connection to HCSR04 sensor
sound_speed = 343 # Sound speed in air in m/s
write_file = 1 # 0 to just print values, 1 to save to text file with file prefix defined above

HCSR04_TrigRx.measure_dist(prefix,interval_ms,record_time,
trigger_pin_num, echo_pin_num, sound_speed, write_file)

"""

#
from machine import RTC, Pin, Timer, unique_id
import utime
from ubinascii import hexlify
from gc import collect
from hcsr04 import HCSR04
from os import rename, listdir
collect()

def measure_dist(prefix='ocn351',interval_ms=100, record_time = 5,trigger_pin_num = 12, echo_pin_num=13, sound_speed=343, write_file = 0):
	global startSampleFlag
	startSampleFlag = 0
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
	print('\nWaiting For Trigger\n')
	while True:
		if startSampleFlag==1:
			startSampleFlag=0
			init_record(runTimer, record_time,interval_ms, sensor,write_file, tmp_file, rtc, datafile, filename)

def RunTrigger(p): # set the trigger):
	global startSampleFlag
	startSampleFlag = 1

def init_record(runTimer, record_time,interval_ms, sensor,write_file, tmp_file, rtc, datafile, filename):
	runTimer.init(period=interval_ms, mode=Timer.PERIODIC, callback=lambda t:record_dist(sensor,write_file, rtc, datafile))
	utime.sleep(record_time) # Sleep and let the timer run for the length of time defined by record_time
	runTimer.deinit() # At the end of our sleep, stop the timer
	if write_file ==1:	# If we've been writing a file...
		datafile.close() # Close the temporary file
		rename(tmp_file,filename) # Rename the temporary file with the filename constructed above

# The actual function taking a measurement and recording the time
def record_dist(sensor,write_file, rtc, datafile): # requires the sensor, real-time clock, and datafile handles, and whether we are writing a file
	led = Pin(2,Pin.OUT)
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

global startSampleFlag
p14 = Pin(14, mode = Pin.IN, pull = Pin.PULL_UP) # define my interrupt input
p14.irq(trigger=Pin.IRQ_RISING, handler=RunTrigger) # set the trigger
