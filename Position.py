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

# Define the target color of the object
target_color1 = Color.RED
target_color2 = Color.Blue
target_color3 = Color.Yellow

# Write your program here.
while True:
    # Move the arm to the designated position
    arm_motor.run_target(300, 60)

    # Lower the claw to pick up the object
    claw_motor.run_target(300, -60)

    # Read the color of the object
    object_color = color_sensor.color()

    # Print the color of the object
    if object_color == target_color1:
        ev3.speaker.say("The object is at the designated position")
    elif object_color == target_color2:
        ev3.speaker.say("The object is at the designated position")
    elif object_color == target_color3: 
         ev3.speaker.say("The object is at the designated position")
    else:
         ev3.speaker.say("The object is at the designated position")

    # If the object is not at the designated position, move the object
    if object_color != target_color:
        # Raise the claw to move the object
        claw_motor.run_target(500, 0)

        # Move the arm back to the starting position
        arm_motor.run_target(500, 0)

        # Wait for the user to move the object
        while color_sensor.color() != target_color:
            wait(10)

        # Lower the claw to release the object
        claw_motor.run_target(500, -60)

        
        