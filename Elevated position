# Move the arm up 90 degrees
arm_motor.run_target(speed=1000, target_angle=90, then=Stop.HOLD, wait=True)

# Open the claw
claw_motor.run_target(speed=1000, target_angle=45, then=Stop.HOLD, wait=True)

# Move the arm down 90 degrees
arm_motor.run_target(speed=1000, target_angle=0, then=Stop.HOLD, wait=True)

# Close the claw
claw_motor.run_target(speed=1000, target_angle=0, then=Stop.HOLD, wait=True)
