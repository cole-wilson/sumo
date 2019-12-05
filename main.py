#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev.ev3 import *
from time import sleep
a = LargeMotor('outB')
print('Moving arm')
a.run_timed(time_sp=1000, speed_sp=750)

m = LargeMotor('outC')
print('sleeping')
sleep(3)
print('driving')
m.run_forever(speed_sp=900)
m.stop(stop_action="hold")
