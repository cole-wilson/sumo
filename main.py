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

colors = {0:'No color',1:'Black',2:'Blue',3:'Green',4:'Yellow',5:'Red',6:'White',7:'Brown'}

us = UltrasonicSensor('in4')
#
# Set motor classes:
arm = LargeMotor('outB')
wheel = LargeMotor('outC')

# Start Program:
print('Finished loading libraries.')
input('Press the Enter key to start the program.')

print('Moving arm for 200 milliseconds.')
arm.run_timed(time_sp=2500, speed_sp=-999)
sleep(1.75)
print('Waiting for Touch Sensor, or Ultrasonic Sensor')

while not(ts1.value() or ts2.value()) or us.value()<250:
    if ts1.value():
        print('TS1')
        break
    elif ts2.value():
        print('TS2')
        break
    elif us.value()<100:
        print('Ultra')
        print(us.value())
        break

    time.sleep(0.5)
    print('\n\n=============')
    print('Touch Sensor 1 state:' + str(ts1.value()))
    print('Touch Sensor 2 state:' + str(ts2.value()))
    try:
        print('Light Sensor: ' + colors[ls.value()])
    except KeyError:
        print('Light Sensor: Key Error')
    print(str(us.value())+'mm')
wheel.run_forever(speed_sp=-999)
while True:
    if not(ts2.value() or ts1.value() or us.value()<100):
        wheel.stop(action='hold')


print('Done')
input()