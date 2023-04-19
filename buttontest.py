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


def reset_robot():
    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)

    claw_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)

    motor_turn.run_until_stalled(300, then=Stop.HOLD, duty_limit=15)

    claw_motor.run_target(speed=100, target_angle=-70, then=Stop.HOLD, wait=True)


def pick_angle(pickangle):
    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    motor_turn.run_target(speed=100, target_angle=pickangle, then=Stop.HOLD, wait=True)

    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=100)

    claw_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=100)

    arm_motor.run_target(speed=100, target_angle=-300)

    motor_turn.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)

    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=100)

    claw_motor.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)


while True:
    # Check which buttons are pressed
    pressed = ev3.buttons.pressed() 
    # 90 degreeif the Up button is pressed
    if Button.UP in pressed:
        pick_angle(-300)
        reset_robot()
    # 135 degree if the Down button is pressed
    elif Button.DOWN in pressed:
        pick_angle(-450)
        reset_robot()
    # 180 degree if the Left button is pressed
    elif Button.LEFT in pressed:
        pick_angle(-600)
        reset_robot()
    else:
        wait(10000)
        ev3.speaker.say("No button pressed turning off")


wait(10)