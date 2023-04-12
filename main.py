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
turning_motor = Motor(Port.C) 
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)

# Write your program here.
ev3.speaker.beep()  
arm_motor.control.limits(speed=100, acceleration=100)
claw_motor.control.limits(speed=100, acceleration=100)

def basic_pickup():
    turning_motor.run_target(speed=100, target_angle=0)
    #Down
    arm_motor.run_target(speed=100, target_angle=-90)#Determine correct target
    #Bite
    claw_motor.run_target(speed=100, target_angle=90) 
    #Up
    arm_motor.run_target(speed=100, target_angle=0)#Determine correct target

def color_analyzer():
    turning_motor.run_target(speed=100, target_angle=0)
    #Down
    arm_motor.run_target(speed=100, target_angle=-90)#Determine correct target
    #Bite
    claw_motor.run_target(speed=100, target_angle=90) 
    #Up
    arm_motor.run_target(speed=100, target_angle=0)#Determine correct target
    #color 
    color = color_sensor.color()
    # Speak the detected color
    if color == Color.BLACK:
        print("The object is black")
    elif color == Color.BLUE:
        print("The object is blue")
    elif color == Color.GREEN:
        print("The object is green")
    elif color == Color.YELLOW:
        print("The object is yellow")
    elif color == Color.RED:
        print("The object is red")
    elif color == Color.WHITE:
        print("The object is white")
    else:
        print("The object color is unknown")

def basic_drop():
    claw_motor.run_time(speed=100, time=1000, then=Stop.HOLD)
    #Opens the claw

    claw_motor.run_time(speed=-1000, time=500, then=Stop.HOLD)
    #Close the claw to reset it

def detection():
    #fsadf

def main_menu():
    while True:
        print("Please pick a Task for mr.robot")
        choice = input("Enter your choice: ")
        if choice == '1':
            Basic_pickup()
        elif choice == '2':
            color_analyzer()
            pass
        elif choice == '3':
            detection()
            pass
        elif choice == '4':
            break
        else:
            ev3.speaker.say("Invalid choice")

main_menu()
