#
#  Collect data from an HCSR04 ultrasonic sensor by defining the sample interval
#  and total time to record.  Write a file if requested.
#
from machine import RTC, Pin, unique_id
import utime
from ubinascii import hexlify
from gc import collect
from hcsr04 import HCSR04
from os import rename
collect()      # Free up heap space

"""
#  An example of a typical execution sequence:
#---------------------------------------
# Sampling parameters
#---------------------------------------

import record_distance

prefix = 'NAME'
interval_ms = 1 # sampling interval in milliseconds, 100 is 10Hz
record_time = 10 # time to record in seconds
trigger_pin_num = 12 # trigger pin connection to HCSR04 sensor
echo_pin_num = 14 # echo pin connection to HCSR04 sensor
sound_speed = 343 # Sound speed in m/s
write_file = 1

record_distance.record_dist(prefix,interval_ms,record_time, trigger_pin_num, echo_pin_num, sound_speed, write_file)

"""

def record_dist(prefix='NAME',interval_ms=100,record_time=10, trigger_pin_num = 12, echo_pin_num=14, sound_speed=343, write_file = 1):
	rtc = RTC()
	sensor = HCSR04(trigger_pin = trigger_pin_num, echo_pin = echo_pin_num, c=sound_speed)
	print('\nUsing sampling interval ',interval_ms,' milliseconds...')
	print('Recording data for ',record_time,' seconds...\n')
	ID=hexlify(unique_id()).decode('utf-8') # Unique ID of the microprocessor
	tmp_file='tmp.txt'  # A temporary filename; we will write partial data to this file, and rename only if sampling
	datafile=open(tmp_file,'w')
	print('\n\n****Beginning Recording ****\n\n')

	timestamp=str(utime.mktime(rtc.datetime()))
	if write_file ==1:
		filename=prefix+'_'+ID+'_'+timestamp+'.txt'
		print('\nCreating data file: ',filename)
	sample_num = (record_time*1000)/100

	for sample in range(sample_num+1):
		t_onboard=rtc.datetime()
		dist = sensor.distance()
		data_str=''
		print(dist)
		if write_file ==1:
			for t in [sample,t_onboard[0],t_onboard[1],t_onboard[2],t_onboard[4],t_onboard[5], \
						   t_onboard[6],t_onboard[7], dist]:
				data_str+='{} '.format(t)
			if sample==0:
				datafile=open(tmp_file,'w')
			else:				# If the first sample, overwrite old tmp_file if it exists
				df=datafile.write("%s\n" % data_str) # df contains the "result" of the write statement (success or failure)

		else:
			print(sample,t_onboard[0],t_onboard[1],t_onboard[2],t_onboard[3],t_onboard[4],t_onboard[5], \
						  t_onboard[6],t_onboard[7], dist)
		if sample<sample_num:  # Sleep only if another sample is to be taken
			utime.sleep_ms(interval_ms)

		#---------------------------------------
		# Done with the comparison loop; change the temporary filename to the permanent one, now that sampling is complete
	if write_file ==1:	#---------------------------------------
		datafile.close()
		rename(tmp_file,filename)
