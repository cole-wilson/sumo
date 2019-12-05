#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev.ev3 import *
from time import sleep
a = LargeMotor('outB')
a.run_timed(time_sp=1000, speed_sp=-750)

m = LargeMotor('outC')
sleep(3)
m.run_forever(speed_sp=900)
m.stop(stop_action="hold")
