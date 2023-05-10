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

# Testing

# Drop off item
#def basic_drop():
    #claw_motor.run_time(speed=100, time=1000, then=Stop.HOLD)
    #Opens the claw

    #claw_motor.run_time(speed=-1000, time=500, then=Stop.HOLD)
    #Close the claw to reset it

# def elevated_position():
#     # Move the arm up 90
#     arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

#     # Move to middle
#     motor_turn.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

#     # Move to object
#     arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=10)

#     # Close the claw
#     claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=50)

#     # Move the arm up 90 degrees
#     arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

#     # Move reset position
#     motor_turn.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)

#     # Move the arm down to ground level 
#     arm_motor.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)

#     # Open the claw
#     claw_motor.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)
    
def pickup_zones():
        # Move the arm up 90
    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    # Move to middle
    motor_turn.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    # Move to object
    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=10)

    # Close the claw
    claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=50)

    # Move the arm up 90 degrees
    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    position = int(input('Which position to drop off:\n1 for 135 degrees\n2 for 180 degrees\n'))
    if position == 1:
        motor_turn.run_target(speed=100, target_angle=-450, then=Stop.HOLD, wait=True)
        arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=10)
        claw_motor.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)
        arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)
        motor_turn.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)
    elif position == 2:
        motor_turn.run_target(speed=100, target_angle=-600, then=Stop.HOLD, wait=True)
        arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=10)
        claw_motor.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)
        arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)
        motor_turn.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)


pickup_zones()
