# UW Oceanography Introduction to Environmental Monitoring and Technology (OCEAN 161)
This repository contains materials required to conduct the bathymetry lab acoustic sensor table top acitvity and lesson plan. This was conducted in a 100-level introductory oceanography course which focused on exploring tools and techniques scientists use to monitor the ocean and environment. This course is geared towards students with no prior oceanography or technology knowledge and enrolls many non-science majors. 

### Lab activity
`StudentWorksheet.docx` is the student activity sheet that walks through the lab procedure to build, calibrate, and simulate use to map bathymetry at two different spatial resolutions. The lab acitivity requires the `GraphingTemplate.xlsx` where students input their collected data and the template graphs it automatically to better facilitate data interpreatation and discussion. 

### Lab Preparation
To prepare for the lab, instructors must acquire the necessary parts and construct bathymetry boxes. In this iteration bathymetry boxes were constucted using black foam board and a seafloor feature was created within the box also using foam board. See photos below for top and side views od bathymetry boxes. 

![topView](https://user-images.githubusercontent.com/9730515/175186565-7aa4f475-b383-4800-9e97-2d69afab3c4b.jpg)    ![sideView](https://user-images.githubusercontent.com/9730515/175186629-ec7489cd-8494-4a92-8e7f-b0ec2d1cc08e.jpg)

Electronic components needed include a Pyboard (or other microcontroller running MicroPython), jumper wires, and an hcsr-04 acoustic sensor. The microcontroller needs to be loaded with `hcsr04.py` and `distance_sensor.py`. Provided here are a file to 3D print a holder for the sensor, `SensorHolder.stl`,  to be able to slide it over the bathymetry box and create the table top bathymetry boxes required for the lab. Other materials needed include a ruler to calibrate the sensor, and an index card.

