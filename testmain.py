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

arm_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
motor_turn = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
arm_motor.control.limits(speed=60, acceleration=120)
motor_turn.control.limits(speed=60, acceleration=120)
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S2)
claw_motor = Motor(Port.A)

# Write your program here.
ev3.speaker.beep() 

arm_position = []
rotation_position = []


def arm_reset():
    arm_motor.run_target(60, 90)
    arm_motor.hold()

ev3.buttons.pressed()
banan = 0
while banan < 10:
    try:
        if str(ev3.buttons.pressed()[0]) == "Button.UP":
            arm_motor.run(15)
        elif str(ev3.buttons.pressed()[0]) == "Button.DOWN":
            arm_motor.run(-15)
        elif str(ev3.buttons.pressed()[0]) == "Button.RIGHT":
            motor_turn.run(-15)
        elif str(ev3.buttons.pressed()[0]) == "Button.LEFT":
            motor_turn.run(15)
        elif str(ev3.buttons.pressed()[0]) == "Button.CENTER":
            arm_position.append(arm_motor.angle())
            rotation_position.append(motor_turn.angle())
            wait(2000)
            arm_reset()

    except:
        print("No button pressed")
        motor_turn.hold()
        arm_motor.hold()


    wait(1000)