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


# Write your program here.
ev3.speaker.beep()

ev3 = EV3Brick()
turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)



color = color_sensor.color()
# Speak the detected color
if color == Color.BLACK:
    ev3.speaker.say("The object is black")
elif color == Color.BLUE:
    ev3.speaker.say("The object is blue")
    motor_turn.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)
    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)
elif color == Color.GREEN:
     ev3.speaker.say("The object is green")
elif color == Color.YELLOW:
    ev3.speaker.say("The object is yellow")
    motor_turn.run_target(speed=100, target_angle=-450, then=Stop.HOLD, wait=True)
    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)
elif color == Color.RED:
    ev3.speaker.say("The object is red")
    motor_turn.run_target(speed=100, target_angle=-600, then=Stop.HOLD, wait=True)
    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)

elif color == Color.WHITE:
    ev3.speaker.say("The object is white")
else:
    ev3.speaker.say("The object color is unknown")
