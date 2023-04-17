from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Create your objects here.
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)

# Define the target color of the object
target_color1 = Color.RED
target_color2 = Color.Blue
target_color3 =Color.Yellow

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
        print("The object is at the designated position")
     elif object_color==target_color2: 
        print("The bject is at the designated position")
       elif object_color==target_color3: 
         print("The bject is at the designated position")
    else:
        print("The object is not at the designated position")

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

