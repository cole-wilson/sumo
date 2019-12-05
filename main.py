#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

input('enter to start')

a = LargeMotor('outB')
print('Moving arm')
a.run_timed(time_sp=1000, speed_sp=750)

m = LargeMotor('outC')
print('sleeping')
sleep(3)
print('driving')

m.run_timed(time_sp=3000, speed_sp=-999)
