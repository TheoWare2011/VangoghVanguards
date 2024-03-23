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
#code for pedestool
drive_base.settings(turn_rate=50)
drive_base.straight(250)
drive_base.turn(-46)
drive_base.straight(960)
#front_motor.run_angle(330,233)
##code for the light house
drive_base.turn(-40)
back_motor.run_angle(234,-440)
#drive_base.turn(-14)
drive_base.straight(-380)

back_motor.run_angle(100,575)
back_motor.run_angle(200,-200)
##code for the magician
drive_base.straight(110)
#drive_base.turn(-87)
#drive_base.straight(-50)
drive_base.turn(-87)
drive_base.straight(563)
#drive_base.turn(16)
front_motor.run_angle(450,-340)
drive_base.straight(-50)
drive_base.turn(-57)
drive_base.straight(725)