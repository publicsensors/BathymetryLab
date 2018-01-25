import os, glob, datetime
import matplotlib.pyplot as plt

data_directory='C:\\Users\\Robert\\Downloads\\351\\'

file_list=[]
for file in glob.glob(data_directory+"*.txt"):
	file_list.append(file)
print file_list
data_time = []
data_dist = []
for filename in file_list:
	with open(filename,'r') as file:
		for line in file:
			data=line.split(' ')
			
			if len(data[6]) ==1:
				ms = '00'+data[6]
			elif len(data[6]) ==2:
				ms = '0'+data[6]
			elif len(data[6]) ==3:
				ms = data[6]
			
			time = data[0]+'-'+data[1]+'-'+data[2]+' '+data[3]+':'+data[4]+':'+data[5]+'.'+ms
			datetime_object = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
			data_time.append(datetime_object)
			if float(data[7])> -1:
				data_dist.append(float(data[7]))
			else:
				data_dist.append('nan')

fig, ax = plt.subplots()
ax.plot_date(data_time, data_dist, markerfacecolor='CornflowerBlue', markeredgecolor='white')
fig.autofmt_xdate()
ax.set_xlim([data_time[0], data_time[-1:]])
#ax.set_ylim([0, 5])
plt.show()