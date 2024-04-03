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
#code for the dragonS
drive_base.settings(straight_speed=300,straight_acceleration=800)
drive_base.straight(315)
drive_base.turn(-38)
drive_base.straight(35)
front_motor.run_angle(500,-420)

drive_base.straight(-237)
# moving towards the sound mixer
drive_base.turn(70) 
drive_base.settings(straight_speed=211,straight_acceleration=800)
drive_base.straight(210)
front_motor.run_angle(100,120)
drive_base.straight(40)

front_motor.run_angle(100,120)
front_motor.run_angle(800,-225)
drive_base.straight(-60)
drive_base.turn(93)
front_motor.run_angle(400,246)
 
drive_base.straight(275) ## INCREASE FROM 240 TO 260 
front_motor.run_angle(400,-400)
drive_base.straight(-180)
front_motor.run_angle(400,260)
drive_base.turn(-87)
drive_base.straight(-360)



