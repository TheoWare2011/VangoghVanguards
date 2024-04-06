from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task


# Choose a letter.
selected = hub_menu(1,2,3,4,5,6,7)

# Based on the selection, run a program.
if selected == 1:
    import Run_1 #Colleact Noah, Museum, Light sound, VR, 3D immersive
elif selected == 2:
    import Run_2
elif selected == 3:
    import Run_3
elif selected == 4:
    import Run_4
elif selected == 5:
    import Run_5
elif selected == 6: 
    import Run_6
elif selected == 7: 
    SystemExit
