from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask

hub = PrimeHub()
#Initialisate the robot 
# Step 1 - Initialize the drive base 
# Step 2 - Initialize the front and back motors 
# Step 3 - Initialize the left and right color sensors in the front
#---------------------------------------------------------------------

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)

# Initialize the drive base. 
# In our robot, the wheel diameter is 88mm.
# The distance between the two wheel-ground contact points is 145mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=145)
# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

#Initialize the front abnd back motors 
front_motor = Motor(Port.D)
back_motor = Motor(Port.C)

# Initialize the color sensors.
right_sensor = ColorSensor(Port.F)
left_sensor = ColorSensor(Port.E)

#------------------------------------------
# Code for the Missions
#------------------------------------------
# moving to emily

drive_base.straight(250)
drive_base.turn(-49)
drive_base.straight(390)
drive_base.turn(65)
drive_base.straight(670)
#picked up emily
#not to let off
drive_base.settings(turn_rate=95)
drive_base.turn(-59)
drive_base.straight(140)  
drive_base.turn(52)
drive_base.straight(260)
drive_base.turn(-79)
drive_base.straight(294)
drive_base.turn(-69)
drive_base.straight(300)
drive_base.turn(-45)
drive_base.straight(685)
drive_base.turn(90)
drive_base.straight(34)
#drive_base.turn(-21)
front_motor.run_angle(400,-769)
wait(200)
front_motor.run_angle(600,310)