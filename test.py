'''
    File name: test.py
    Author: Jairo Moreno
    Date created: 20/11/2018
    Date last modified: 22/11/2018
    Python Version: 3.6
'''

import mzstepper
import time
import random

StepPins =  [26,19,13,6]
obj = mzstepper.Stepper(StepPins, 0, 2000, 0.001, True, True)

print("pos: 100")
obj.SetPosPercent(100)
for x in range(10):
    pos = random.randint(1, 100)
    print("pos: "+str(pos)+" - "+str(obj.GetPos()) )
    obj.SetPosPercent(pos)
    time.sleep(1)

print("pos : 0")
obj.SetPosPercent(0)
time.sleep(3)
obj.Disable()
time.sleep(1)
