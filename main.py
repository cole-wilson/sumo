#!/usr/bin/env python3
# So program can be run from Brickman
from ev3dev.ev3 import *
from time import sleep
import os
#TODO: update sensors on physical robot.

# Set sensor classes:
ts1 = TouchSensor('in1')
ts2 = TouchSensor('in2')
ls = ColorSensor('in3')
us = UltrasonicSensor('in4')
#
# Set motor classes:
arm = LargeMotor('outB')
wheel = LargeMotor('outC')

# Start Program:
print('Finished loading libraries.')
input('Press the Enter key to start the program.')

print('Moving arm for 200 milliseconds.')
arm.run_timed(time_sp=200, speed_sp=999)
sleep(0.75)
print('Waiting for Touch Sensor, or Ultrasonic Sensor')

while not(ts1.value() or ts2.value()) or (us.value()<100) :
    os.system('clear')
    print('-------------------')
    print('|' + '        ' if ts1.value() else '+++++++' + '|        |')
    print('|        |        |')
    print('|        |        |')
    print('-------------------')


wheel.run_timed(time_sp=3000, speed_sp=-999)


print('Done')
input()