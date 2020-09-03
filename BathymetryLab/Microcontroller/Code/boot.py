# This file is executed on every boot (including wake-boot from deepsleep)
from gc import collect
collect()

# If we wanted to initiate a file on wakeup, we would include it in main
#import main.py 
