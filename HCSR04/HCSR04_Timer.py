#
#  Example code to assess accuracy and precision of on-board and external RTCs relative to an NTP server.
# 
from machine import RTC, Pin, Timer, unique_id
import utime
from ubinascii import hexlify
from gc import collect
from hcsr04 import HCSR04
from os import rename, listdir
collect()      # Free up heap space 

"""
#  An example of a typical execution sequence:
#---------------------------------------
# Sampling parameters
#---------------------------------------

import DistSave2

prefix = 'robert'
interval_ms = 100 # sampling interval in milliseconds, 100 is 10Hz
record_time = 10 # time to record in seconds
trigger_pin_num = 12 # trigger pin connection to HCSR04 sensor
echo_pin_num = 14 # echo pin connection to HCSR04 sensor
sound_speed = 343 # Sound speed in m/s
write_file = 0

DistSave2.measure_dist(prefix,interval_ms,record_time, trigger_pin_num, echo_pin_num, sound_speed, write_file)

"""

def measure_dist(prefix='ocn351',interval_ms=100,record_time=10, trigger_pin_num = 12, echo_pin_num=14, sound_speed=343, write_file = 0):
	sensor = HCSR04(trigger_pin = trigger_pin_num, echo_pin = echo_pin_num, c=sound_speed)
	print('\nUsing sampling interval ',interval_ms,' milliseconds...')
	print('Recording data for ',record_time,' seconds...\n')
	print('\n\n****Beginning Recording ****\n\n')
	runTimer = Timer(-1)
	tmp_file='tmp.txt'  # A temporary filename; we will write partial data to this file, and rename only if sampling 
	rtc = RTC()
	ID=hexlify(unique_id()).decode('utf-8') # Unique ID of the microprocessor
	timestamp=str(utime.mktime(rtc.datetime()))
	filename=prefix+'_'+ID+'_'+timestamp+'.txt'
	if write_file ==1:
		print('\nCreating data file: ',filename,'\n\n')
		datafile=open(tmp_file,'w')  # If the first sample, overwrite old tmp_file if it exists
	else:
		datafile=''
		print('\nNot writing data to file\n')
	runTimer.init(period=interval_ms, mode=Timer.PERIODIC, callback=lambda t:record_dist(sensor,write_file, tmp_file, rtc, datafile))
	utime.sleep(record_time)
	runTimer.deinit()
	if write_file ==1:	#---------------------------------------
		datafile.close()
		rename(tmp_file,filename)

	
	
def record_dist(sensor,write_file, tmp_file, rtc, datafile):
	t_onboard=rtc.datetime()
	dist = sensor.distance()
	if write_file ==1:
		data_str=''
		for t in [t_onboard[0],t_onboard[1],t_onboard[2],t_onboard[4],t_onboard[5],t_onboard[6],t_onboard[7], dist]:
			data_str+='{} '.format(t)
		df=datafile.write("%s\n" % data_str)

	print(t_onboard[0],t_onboard[1],t_onboard[2],t_onboard[4],t_onboard[5],t_onboard[6],t_onboard[7], dist)

