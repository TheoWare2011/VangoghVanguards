#Dropping Experts and Audience in different areas

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
# Code for the robot
#------------------------------------------

#Gone to drop off Noah---------------------
drive_base.straight(420)
drive_base.turn(-18)
drive_base.straight(440)

 #------------------------------------------
 #dropped of Noah
 #------------------------------------------
 #Gone to do Virtual reality
 #------------------------------------------
 #----------------------
 #----
 ##Old uneeded code
 #-------------------------------------------
 #drive_base.turn(17)
 #-------------------------------------------

drive_base.straight(-179)
drive_base.turn(-69)
drive_base.straight(892)
drive_base.turn(87)
# -- In prosses of doing VR
drive_base.straight(10)
front_motor.run_angle(300,-420)
front_motor.run_angle(300,420)
drive_base.straight(-170)
#vr done
#------------------------------------------
# Moving to Augmented reality
#------------------------------------------
drive_base.turn(49)
front_motor.run_angle(300,-470)
drive_base.straight(405)
drive_base.turn(60)
#------------------------------------------
# Augmented reality is finshed
#------------------------------------------
# Return back to home
#----
drive_base.straight(90)
# finishing touch on AR
drive_base.turn(-50)
#---- done
drive_base.turn(50)
drive_base.straight(530)
drive_base.turn(61)
drive_base.straight(490)
