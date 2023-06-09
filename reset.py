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


arm_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=70)
claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=50)
motor_turn.run_until_stalled(500, then=Stop.HOLD , duty_limit=15)

claw_motor.reset_angle(0)

# if touch_sensor.pressed() == True:
#     motor_turn.HOLD()

# claw_motor.run_target(speed=100, target_angle=-70, then=Stop.HOLD, wait=True) #högra röda uppåt
claw_motor.run_time(speed=-80, time=1000, then=Stop.HOLD, wait=True) 