import RPi.GPIO as GPIO
import time

class Controller:

    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)
        #physical pin are 31,33,35,37
        Pins = [6,13,19,26]
        self.Pins = Pins
        self.stepState = 0
        for pin in Pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)
            
    def seqSetting(self,arg2):
        
        seq1 = [[1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1],
                [1,0,0,1]]

        seq2 = [[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]]

        seq3 = [[1,0,0,1],
                [1,1,0,0],
                [0,1,1,0],
                [0,0,1,1]]

        tempSeq = [seq1, seq2, seq3]
        return tempSeq[arg2]

    def mainLoop(self, Seq, waitTime, Dir, step, stepCb):
        StepCounter = 0
        microStep = self.stepState
        print (microStep)
        while StepCounter < step:
            j = 0
            for i in Seq[microStep]:
                GPIO.output(self.Pins[j], i)
                j += 1
            if Dir > 0:
                microStep += 1
            else:
                microStep -= 1
            microStep = microStep % len(Seq)
            # Wait before moving on
            time.sleep(waitTime)
            #time to break
            StepCounter += 1

            stepCb(StepCounter)
        self.stepState = microStep
