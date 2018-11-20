'''
    File name: mzstepper.py
    Author: Jairo Moreno
    Date created: 20/11/2018
    Date last modified: 20/11/2018
    Python Version: 3.6
    Based on: https://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/
'''



# Import required libraries
import sys
import time
import RPi.GPIO as GPIO


SeqDef =  [[1,0,0,1],
           [1,0,0,0],
           [1,1,0,0],
           [0,1,0,0],
           [0,1,1,0],
           [0,0,1,0],
           [0,0,1,1],
           [0,0,0,1]]

class Stepper:

    def __init__(self, StepPins, CurrentPos = 0, MaxStep = 2000, WaitTime = 0.5, Debug = False, TurnOff = True, Seq = SeqDef ):
        self.MaxStep = MaxStep
        self.CurrentPos = CurrentPos
        self.WaitTime = WaitTime
        self.StepPins = StepPins
        self.Seq = Seq
        self.TurnOff = TurnOff
        self.Debug = Debug

        GPIO.setmode(GPIO.BCM)
        for pin in self.StepPins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)

    def SetPosPercent(self, NewPosPercent):
        return self.SetPos( int(self.MaxStep  / 100 * float(NewPosPercent)) )


    def SetPos(self, NewPos):
        if NewPos > self.MaxStep:
            return self.CurrentPos

        if NewPos < 0 :
            return self.CurrentPos

        if NewPos == self.CurrentPos :
            return NewPos

        if NewPos < self.CurrentPos :
            StepDir = -1
        else:
            StepDir = 1

        StepCount = len(self.Seq)

        # Initialise variables
        StepCounter = 0

        # Start main loop
        if self.Debug:
           print("while not " + str(NewPos) + " == " + str(self.CurrentPos))

        while not NewPos == self.CurrentPos:
            if self.Debug:
                print(StepCounter)
                print(self.Seq[StepCounter])

            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[StepCounter][pin]!=0:
                    if self.Debug:
                        print(str(self.CurrentPos) + " Enable GPIO %i"  %(xpin))
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            StepCounter += StepDir
            self.CurrentPos += StepDir

            # If we reach the end of the sequence
            # start again
            if (StepCounter>=StepCount):
                StepCounter = 0
            if (StepCounter<0):
                StepCounter = StepCount+StepDir

            # Wait before moving on
            time.sleep(self.WaitTime)

            for pin in self.StepPins:
                GPIO.output(pin, False)
        return self.CurrentPos

    def Disable(self):
        if self.TurnOff:
            for pin in self.StepPins:
                if self.Debug:
                    print("disable pins")
                GPIO.output(pin, False)
