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

def dropoff(angle):
    claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500) #Closes claw

    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True) #Raises the arm

    motor_turn.run_target(speed=100, target_angle=angle, then=Stop.HOLD, wait=True) #Turns the arm x degrees

    arm_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=100) #Lowers the arm

    claw_motor.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True) #Opens the claw

    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True) #Raises the arm

    motor_turn.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True) #Returns arm to 0 degrees

    arm_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500) #Lowers the arm

choice = '4'

while choice != '0':
    choice = input('Which angle do you want to drop off at? Input 1 for 90 degrees, 2 for 135 and 3 for 180 degrees. Input 0 to end the function.')
    if choice == '1':
        dropoff(-300)
    elif choice == '2':
        dropoff(-450)
    elif choice == '3':
        dropoff(-600)



