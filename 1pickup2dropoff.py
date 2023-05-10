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

# Configure the motor that rotates the base. It has a 12-teeth and a
# 36-teeth gear connected to it. We would like positive speed values
# to make the arm go away from the Touch Sensor. This corresponds
# to counterclockwise rotation of the motor.
motor_turn = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

# Limit the elbow and base accelerations. This results in
# very smooth motion. Like an industrial robot.
arm_motor.control.limits(speed=60, acceleration=120)
motor_turn.control.limits(speed=60, acceleration=120)

# Set up the Touch Sensor. It acts as an end-switch in the base
# of the robot arm. It defines the starting point of the base.
touch_sensor = TouchSensor(Port.S1)

# Set up the Color Sensor. This sensor detects when the elbow
# is in the starting position. This is when the sensor sees the
# white beam up close.
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
while banan < 3:
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
            banan += 1
            wait(2000)
            arm_reset()

    except:
        motor_turn.hold()
        arm_motor.hold()


arm_reset() #Raises the arm
motor_turn.run_target(speed=100, target_angle=rotation_position[0], then=Stop.HOLD, wait=True) #Turns the arm to the pickup zone
arm_motor.run_target(speed=100, target_angle=arm_position[0], then=Stop.HOLD, wait=True) #Lowers the arm to the pickup zone
claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500) #Closes claw

arm_reset() #Raises the arm
motor_turn.run_target(speed=100, target_angle=rotation_position[1], then=Stop.HOLD, wait=True) #Turns the arm to the first dropoff zone
arm_motor.run_target(speed=100, target_angle=arm_position[1], then=Stop.HOLD, wait=True) #Lowers the arm to the first dropoff zone
claw_motor.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True) #Opens the claw

arm_reset() #Raises the arm
motor_turn.run_target(speed=100, target_angle=rotation_position[0], then=Stop.HOLD, wait=True) #Turns the arm to the pickup zone
arm_motor.run_target(speed=100, target_angle=arm_position[0], then=Stop.HOLD, wait=True) #Lowers the arm to the pickup zone
claw_motor.run_until_stalled(200, then=Stop.HOLD , duty_limit=500) #Closes claw

arm_reset() #Raises the arm
motor_turn.run_target(speed=100, target_angle=rotation_position[2], then=Stop.HOLD, wait=True) #Turns the arm to the second dropoff zone
arm_motor.run_target(speed=100, target_angle=arm_position[2], then=Stop.HOLD, wait=True) #Lowers the arm to the second dropoff zone
claw_motor.run_target(speed=100, target_angle=0, then=Stop.HOLD, wait=True) #Opens the claw
arm_reset() #Raises the arm






