#!/usr/bin/env python3
# So program can be run from Brickman
from ev3dev.ev3 import *
from time import sleep
input('enter to start')

arm = LargeMotor('outB')
print('Moving arm')
arm.run_timed(time_sp=200, speed_sp=999)

wheel = LargeMotor('outC')
print('sleeping')
sleep(3)
print('driving')

wheel.run_timed(time_sp=3000, speed_sp=-999)
