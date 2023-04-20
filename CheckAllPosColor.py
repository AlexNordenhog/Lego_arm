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



# Speak the detected color
# Create your objects here.
ev3 = EV3Brick()
# turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
motor_turn = Motor(Port.C)
touch_sensor = TouchSensor(Port.S1)


ev3.speaker.beep()
def check_pos_color(pos):
    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)

    # Öppnar claw

    claw_motor.run_time(speed=-80, time=1000, then=Stop.HOLD, wait=True)

    # Går upp

    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)


    # Går till pos 3

    motor_turn.run_target(speed=100, target_angle=pos, then=Stop.HOLD, wait=True)

    # Går ner

    arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)

    # Stänger clown

    claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500)

    # Upp till sensor

    arm_motor.run_target(speed=100, target_angle=-197, then=Stop.HOLD, wait=True)

    wait(2000)
    # Color

        # Speak the detected color
    if color == Color.BLACK:
        ev3.speaker.say("The object is black at position 3")
    elif color == Color.BLUE:
        ev3.speaker.say("The object is blue at position 3")
    elif color == Color.GREEN:
        ev3.speaker.say("The object is green position 3")
    elif color == Color.YELLOW:
        ev3.speaker.say("The object is yellow position 3")
    elif color == Color.RED:
        ev3.speaker.say("The object is red position 3")
    elif color == Color.WHITE:
        ev3.speaker.say("The object is white position 3")
    else:
        ev3.speaker.say("The object color is unknown")

    claw_motor.run_time(speed=-80, time=1000, then=Stop.HOLD, wait=True)  

    arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

    motor_turn.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)



# color = color_sensor.color()

# # Går upp

# arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

# # Går till pos 1

# motor_turn.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

# # Öppnar claw

# claw_motor.run_time(speed=-80, time=1000, then=Stop.HOLD, wait=True)

# # Går ner

# arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)

# # Stänger clown

# claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500)

# # Upp till sensor

# arm_motor.run_target(speed=100, target_angle=-197, then=Stop.HOLD, wait=True)

# wait(2000)
# # Color

#     # Speak the detected color
# if color == Color.BLACK:
#     ev3.speaker.say("The object is black at position 1")
# elif color == Color.BLUE:
#     ev3.speaker.say("The object is blue at position 1")
# elif color == Color.GREEN:
#     ev3.speaker.say("The object is green position 1")
# elif color == Color.YELLOW:
#     ev3.speaker.say("The object is yellow position 1")
# elif color == Color.RED:
#     ev3.speaker.say("The object is red position 1")
# elif color == Color.WHITE:
#     ev3.speaker.say("The object is white position 1")
# else:
#     ev3.speaker.say("The object color is unknown")  

# # Går ner

# arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)

# # Öppnar claw

# claw_motor.run_time(speed=-80, time=1000, then=Stop.HOLD, wait=True)

# # Går till pos 2

# motor_turn.run_target(speed=100, target_angle=-450, then=Stop.HOLD, wait=True)

# # Går ner

# arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)

# # Stänger clown

# claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500)

# # Upp till sensor

# arm_motor.run_target(speed=100, target_angle=-197, then=Stop.HOLD, wait=True)

# wait(2000)
# # Color

#     # Speak the detected color
# if color == Color.BLACK:
#     ev3.speaker.say("The object is black at position 2")
# elif color == Color.BLUE:
#     ev3.speaker.say("The object is blue at position 2")
# elif color == Color.GREEN:
#     ev3.speaker.say("The object is green position 2")
# elif color == Color.YELLOW:
#     ev3.speaker.say("The object is yellow position 2")
# elif color == Color.RED:
#     ev3.speaker.say("The object is red position 2")
# elif color == Color.WHITE:
#     ev3.speaker.say("The object is white position 2")
# else:
#     ev3.speaker.say("The object color is unknown")

# # Går ner

# arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)

# # Öppnar claw

# claw_motor.run_time(speed=-80, time=1000, then=Stop.HOLD, wait=True)

# # Går upp

# arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)


# # Går till pos 3

# motor_turn.run_target(speed=100, target_angle=-600, then=Stop.HOLD, wait=True)

# # Går ner

# arm_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=500)

# # Stänger clown

# claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500)

# # Upp till sensor

# arm_motor.run_target(speed=100, target_angle=-197, then=Stop.HOLD, wait=True)

# wait(2000)
# # Color

#     # Speak the detected color
# if color == Color.BLACK:
#     ev3.speaker.say("The object is black at position 3")
# elif color == Color.BLUE:
#     ev3.speaker.say("The object is blue at position 3")
# elif color == Color.GREEN:
#     ev3.speaker.say("The object is green position 3")
# elif color == Color.YELLOW:
#     ev3.speaker.say("The object is yellow position 3")
# elif color == Color.RED:
#     ev3.speaker.say("The object is red position 3")
# elif color == Color.WHITE:
#     ev3.speaker.say("The object is white position 3")
# else:
#     ev3.speaker.say("The object color is unknown")

# claw_motor.run_time(speed=-80, time=1000, then=Stop.HOLD, wait=True)  

# arm_motor.run_target(speed=100, target_angle=-300, then=Stop.HOLD, wait=True)

# motor_turn.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True)


check_pos_color(-300)
check_pos_color(-450)
check_pos_color(-600)