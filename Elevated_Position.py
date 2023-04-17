#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
# turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
motor_turn = Motor(Port.C)
touch_sensor = TouchSensor(Port.S1)

# Write your program here.
ev3.speaker.beep()  

# Move the arm up 90 degrees
arm_motor.run_target(speed=1000, target_angle=90, then=Stop.HOLD, wait=True)

# Open the claw
claw_motor.run_target(speed=1000, target_angle=45, then=Stop.HOLD, wait=True)

# Move the arm down 90 degrees
arm_motor.run_target(speed=1000, target_angle=0, then=Stop.HOLD, wait=True)

# Close the claw
claw_motor.run_target(speed=1000, target_angle=0, then=Stop.HOLD, wait=True)
