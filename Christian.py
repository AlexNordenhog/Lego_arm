
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

def detection()
    turn = 0
    turning_motors.run_target(speed=100, target_angle=0)
# re-setting the arm
    turning_motor.run_untill_stalled(speed=100, then=Stop.Hold, duty_limit=None)
# Turns untill stop
    angle = angle()
# Angle of the stop
    if angle == 180:
        turn += 0
        turning_motor.run_untill_stalled(speed=-100, then=Stop.Hold, duty_limit=None)
        angle = angle()
        if angle == 180 or angle == -180:
            print("No item found!")
    
    if turn == 0:
        item_angle = angle + 5
    elif turn == 1: 
        item_angle = angle - 5
    
    print(item_angle)

    

        





    


