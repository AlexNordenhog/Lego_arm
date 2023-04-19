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


def test():
    # detected90 = 0
    # detected135 = 0
    # detected180 = 0

    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    motor_turn.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    arm_motor.run_until_stalled(100, then=Stop.HOLD , duty_limit=10)

    claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=50)

    clawang = claw_motor.angle()
    print(claw_motor.angle())
    #Detect 
    if clawang < 85 and clawang > 60:
        # detected90 += 1 
        ev3.speaker.say("No item deteced")
    else:
        ev3.speaker.say("Item found")

    #     arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    #     motor_turn.run_target(speed=100, target_angle=-150, then=Stop.HOLD, wait=True)

    #     arm_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=15)

    #     ang = arm_motor.angle()

    #     if ang < -10:
    #         ev3.speaker.say("Item detected at 135 degrees")
    #     else:
    #         ev3.speaker.say("No item found, Searching 180 degrees")

    #         arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    #         motor_turn.run_target(speed=100, target_angle=-150, then=Stop.HOLD, wait=True)

    #         arm_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=15)

    #         ang = arm_motor.angle()

    #         if ang < -10:
    #             ev3.speaker.say("Item detected at 180 degrees")
    #         else: 
    #             ev3.speaker.say("No item found")
        


    # arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    # motor_turn.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    # arm_motor.run_until_stalled(100, then=Stop.HOLD , duty_limit=10)

    # ang = arm_motor.angle()


def detect_item():
    
    clawang = claw_motor.angle()

    print(claw_motor.angle())

    if clawang < 85 and clawang > 60: 
        ev3.speaker.say("No item deteced")

    else:
        ev3.speaker.say("Item found")


def check_angle(angle):
    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    motor_turn.run_target(speed=100, target_angle=angle, then=Stop.HOLD, wait=True)

    arm_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=10)

    claw_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)

    detect_item()

    reset_robot()


def reset_robot():
    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)

    claw_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)

    motor_turn.run_until_stalled(300, then=Stop.HOLD, duty_limit=15)

    claw_motor.run_target(speed=100, target_angle=-70, then=Stop.HOLD, wait=True)


reset_robot()
check_angle(-300)
check_angle(-450)
check_angle(-600)
