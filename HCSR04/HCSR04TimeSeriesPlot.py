#
# Reads and plots time series of distance data recorded in text file
# using HCSR04_Timer.py or HCSR04_SampleCt.py
#
import numpy as np
import os, glob, datetime
import matplotlib.pyplot as plt
from scipy import interpolate

from scipy import signal
from matplotlib import mlab

#------ USER DEFINED PARAMETER---------
## Change the path for data_directory below to match the path of your .txt file
## containing the output from your HCSR04


data_directory='path'
#--------------------------------------

plt.ion() # interactive plotting turned on

file_list=[] # setup the variable to contain the file names
for file in glob.glob(data_directory+"*.txt"): # find all of the .txt files
    filename = file # add the files to a list
    data_time = [] # create a variable to hold the measurement time
    data_dist = [] # create a variable to hole the measurement value
    with open(filename,'r') as file: # open the file
        for line in file: # for each line of data in the file
            data=line.split(' ') # use a space as the delimeter
            # Since the 7th value in the data table is the ms value of time,
            # it can range from 0 to 999, so we want to make sure our code knows
            # how to  treat '90'ms as '090'ms and not '900' or '9'ms
            if len(data[6]) ==1:
                ms = '00'+data[6]
            elif len(data[6]) ==2:
                ms = '0'+data[6]
            elif len(data[6]) ==3:
                ms = data[6]
            # Create a single string of the time values
            time = data[0]+'-'+data[1]+'-'+data[2]+' '+data[3]+':'+data[4]+':'+data[5]+'.'+ms
            # Convert the time string to a datetime value
            datetime_object = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
            data_time.append(datetime_object) # Append the datetime to our list of times
            data_dist.append(float(data[7])) # Append the measurement to our list of distances


        # Now we're going to make a Figure
        Ffig=plt.figure()  # Create a new graphics window

        # On the top axes, plot the raw data:
        Fax1 = Ffig.add_subplot(211) # subplot #1
        Fax1.plot_date(data_time, data_dist, markerfacecolor='CornflowerBlue', markeredgecolor='white') # plot our data
        Ffig.autofmt_xdate() # Tell python the x-ticks are datetime values
        plt.title(filename) # lets keep track of what we're plotting
        Fax1.set_xlim([data_time[0], data_time[-1:]]) # Set the x-axis to range from our earliest to latest datetime value

        # Now plot the correlation after detrending the raw data
        Fax2 = Ffig.add_subplot(212) # subplot #2
        Fax2.acorr(data_dist, usevlines=False, detrend=mlab.detrend_linear,normed=True, maxlags=35, lw=1)
        Fax2.grid(True)
        Fax2.axhline(0, color='black', lw=1)

        plt.show(block=True) # Show the figure
        input("Paused. Press <return> to proceed...") # keep the figure open till we're done, for python 3
        #raw_input("Paused. Press <return> to proceed...") # for python 2
