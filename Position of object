# Import necessary libraries
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Create your objects here.
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
distance_sensor = UltrasonicSensor(Port.S3)

# Write your program here.
while True:
    # Move the arm to the position above the object
    arm_motor.run_target(500, 30)

    # Lower the claw to pick up the object
    claw_motor.run_target(500, -60)

    # Read the distance to the object
    object_distance = distance_sensor.distance()

    # Print the distance to the object
    print("Distance to object: ", object_distance)

    # If the object is within range of the distance sensor, move the object
    if object_distance < 100:
        # Read the color of the object
        object_color = color_sensor.color()

     color = color_sensor.color()
       Speak the detected color
 if color == Color.BLACK:
    ev3.speaker.say("The object is black")
 elif color == Color.BLUE:
     ev3.speaker.say("The object is blue")
  elif color == Color.GREEN:
     ev3.speaker.say("The object is green")
 elif color == Color.YELLOW:
    ev3.speaker.say("The object is yellow")
   elif color == Color.RED:
    ev3.speaker.say("The object is red")
   elif color == Color.WHITE:
     ev3.speaker.say("The object is white")
 else:
     ev3.speaker.say("The object color is unknown")

        # Raise the claw to move the object
        claw_motor.run_target(500, 0)

        # Move the arm back to the starting position
        arm_motor.run_target(500, 0)

        # Wait for the user to move the object
        while distance_sensor.distance() < 100:
            wait(10)

        # Lower the claw to release the object
        claw_motor.run_target(500, -60)

