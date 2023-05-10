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
motor_turn = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)


# Write your program here.
ev3.speaker.beep()

import datetime

def pickup(angle):
    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True) #Raises the arm

    motor_turn.run_target(speed=100, target_angle=angle, then=Stop.HOLD, wait=True) #Turns the arm x degrees

    arm_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500) #Lowers the arm

    claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500) #Closes claw

    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True) #Raises the arm again

    motor_turn.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True) #Returns arm to 0 degrees

    arm_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500) #Lowers the arm

    claw_motor.run_target(speed=100, target_angle=-70, then=Stop.HOLD, wait=True) #Opens the claw

# Set the time to sort items (24-hour format)
sort_time = "10:42"

# Loop until the sort time is reached
while True:
    # Get the current time in 24-hour format
    # current_time = ev3.time().strftime("%H:%M")
    current_time = datetime.datetime.now().strftime("%H:%M")

    # Check if it's time to sort the items
    if current_time == sort_time:
        ev3.speaker.say("TIMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        break
    else:
        print("haba")
        wait(10000)
        continue
    

    # Wait for 1 minute before checking the time again
    wait(30000)
