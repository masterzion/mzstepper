'''
    File name: test.py
    Author: Jairo Moreno
    Date created: 20/11/2018
    Date last modified: 20/11/2018
    Python Version: 3.6
'''

import mzstepper

StepPins =  [26,19,13,6]
obj = mzstepper.Stepper(StepPins, 0, 2000, 0.001, True)
print(obj.SetPosPercent(90) )
print(obj.SetPosPercent(20) )
obj.Disable()
